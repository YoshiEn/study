import urllib
import json

class KameWeater():
	def __init__(self):
		pass
	
	def return_kame_weater(self,message):
		url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
		city_name = (message.body['text'])[9:]
		if city_name in {'茨城','水戸'}:
			city_id = '080010'
		elif city_name in '土浦':
			city_id = '080020'
		elif city_name in {'栃木','宇都宮'}:
			city_id = '090010'
		elif city_name in '大田原':
			city_id = '090020'
		elif city_name in {'群馬','前橋'}:
			city_id = '100010'
		elif city_name in 'みなかみ':
			city_id = '100020'
		elif city_name in {'埼玉','さいたま'}:
			city_id = '110010'
		elif city_name in '熊谷':
			city_id = '110020'
		elif city_name in '秩父':
			city_id = '110030'
		elif city_name in '千葉':
			city_id = '120010'
		elif city_name in '銚子':
			city_id = '120020'
		elif city_name in '館山':
			city_id = '120030'
		elif city_name in '東京':
			city_id = '130010'
		elif city_name in {'大島','伊豆諸島'}:
			city_id = '130020'
		elif city_name in '八丈島':
			city_id = '130030'
		elif city_name in {'父島','小笠原諸島'}:
			city_id = '130040'
		elif city_name in {'神奈川','横浜'}:
			city_id = '140010'
		elif city_name in '小田原':
			city_id = '140020'
		elif city_name in {'山梨','甲府'}:
			city_id = '190010'
		elif city_name in '河口湖':
			city_id = '190020'
		else:
			city_id = ''
			
		if city_id != '':
			html = urllib.request.urlopen(url + city_id)
			jsonfile = json.loads(html.read().decode('utf-8'))
			title = jsonfile['title'] 
			telop = jsonfile['forecasts'][0]['telop']
			#telopが晴れだったら晴れのスラックのアイコンとか場合分け
			telop_icon = ''
			if telop.find('雪') > -1:
				telop_icon = ':showman:'
			elif telop.find('雷') > -1:
				telop_icon = ':thinder_cloud_and_rain:'
			elif telop.find('晴') > -1:
				if telop.find('曇') > -1:
					telop_icon = ':partly_sunny:'
				elif telop.find('雨') > -1:
					telop_icon = ':partly_sunny_rain:'
				else:
					telop_icon = ':sunny:'
			elif telop.find('雨') > -1:
				telop_icon = ':umbrella:'
			elif telop.find('曇') > -1:
				telop_icon = ':cloud:'
			else:
				telop_icon = ':fire:'
			text = title + '\n' + '今日の天気　' + telop + telop_icon
		else:
			if city_name in {'にほん', 'にっぽん' ,'日本' ,'japan', 'Japan', 'JAPAN'}:
				text = '知るかボケ！'
			elif city_name in '高野':
				text = ':kono_yobu_toki_sennyou_special:ほう、この私を見つけるとはやるな:kono_yobu_toki_sennyou_special:'
			else:
				text = '\''+ city_name + '\'ちょっとわからないなぁ\n関東限定、常識の範囲内でお願い！\nピンポイント検索はまた後日！'
		
		message.send(text) 