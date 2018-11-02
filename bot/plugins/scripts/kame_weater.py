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
			if city_name in '日本':
				text = '日本国（にほんこく、にっぽんこく）、または日本（にほん、にっぽん）は、東アジアに位置する日本列島（北海道・本州・四国・九州の主要四島およびそれに付随する島々）及び、南西諸島・伊豆諸島・小笠原諸島などから成る島国。'
				text += '「日本」という漢字による国号の表記は、日本列島が中国大陸から見て東の果て、つまり「日の本（ひのもと）」に位置することに由来するのではないかとされる。近代の二つの憲法の表題は、「日本国憲法」および「大日本帝国憲法」であるが、国号を「日本国」または「日本」と直接かつ明確に規定した法令は存在しない。ただし、日本工業規格 (Japanese Industrial Standard) では日本国、英語表記をJapanと規定。更に、国際規格 (ISO) では3文字略号をJPN、2文字略号をJPと規定している。また、日本国外務省から発給される旅券の表紙には「日本国」の表記と十六一重表菊を提示している。法令で日本を指し示す表記には統一されておらず日本、日本国、本邦、わが国、などが混在している。'
				text += '「にっぽん」、「にほん」と読まれる。どちらも多く用いられているため、日本政府は正式な読み方をどちらか一方には定めておらず、どちらの読みでも良いとしている。7世紀の後半の国際関係から生じた「日本」国号は、当時の国際的な読み（音読）で「ニッポン」（呉音）ないし「ジッポン」（漢音）と読まれたものと推測される。いつ「ニホン」の読みが始まったか定かでない。仮名表記では「にほん」と表記された。平安時代には「ひのもと」とも和訓されるようになった。室町時代の謡曲・狂言は、中国人に「ニッポン」と読ませ、日本人に「ニホン」と読ませている。安土桃山時代にポルトガル人が編纂した『日葡辞書』や『日本小文典』等には、「ニッポン」「ニホン」「ジッポン」の読みが見られ、その用例から判断すると、改まった場面・強調したい場合に「ニッポン」が使われ、日常の場面で「ニホン」が使われていた。このことから小池清治は、中世の日本人が中国語的な語感のある「ジッポン」を使用したのは、中国人・西洋人など対外的な場面に限定されていて、日常だと「ニッポン」「ニホン」が用いられていたのでは、と推測している。なお、現在に伝わっていない「ジッポン」音については、その他の言語も参照。近代以降も「ニッポン」「ニホン」両方使用される中、1934年には文部省臨時国語調査会が「にっぽん」に統一して外国語表記もJapanを廃してNipponを使用するという案を示したこともあったが、不完全に終わった。同年、日本放送協会（NHK）は「放送上、国号としては『にっぽん』を第一の読み方とし、『にほん』を第二の読み方とする」旨の決定をした。その後現在も両方使用されており、2009年6月30日に政府は、「『にっぽん』『にほん』という読み方については、いずれも広く通用しており、どちらか一方に統一する必要はない」とする答弁書を閣議決定している。現在、通商や交流の点で自国外と関連のある紙幣、切手などには「NIPPON」と描かれ（紙幣発券者も「にっぽんぎんこう」である）ているほか、NHK、日本テレビ、ニッポン放送、日本武道館、全日本空輸、近畿日本鉄道、西日本鉄道、日本体育大学、日本郵便、NEXCO東日本・NEXCO中日本・NEXCO西日本、日本電気、日本電信電話、日本郵船、日本通運、NTT東日本・NTT西日本などで「NIPPON」（にっぽん）表記を用いる一方、「NIHON」（にほん）表記を用いる例は、日本大学、日本航空、日本経済新聞、日本たばこ産業、JR東日本・JR西日本、日本ユニシス、日本相撲協会、日本交通、日本オリンピック委員会、NTT東日本、などがある。日本経済新聞が2016年に行った調査によると、社名に「日本」が含まれる上場企業の読み方は、「にほん」が60%、「にっぽん」が40%であり、「にっぽん」と読ませる企業の比率が増加傾向にあった。テレビ番組名では「にっぽん」が使われることが多くなってきている。なお、日本国憲法の読みについて、内閣法制局は、読み方について特に規定がなく、どちらでもよいとしている。憲法制定の際、読みについての議論で担当の金森徳次郎国務大臣は「ニホン、ニッポン両様の読み方がともに使われることは、通念として認められている」と述べており、どちらかにはされなかった。日本のオリンピック選手団は入場行進時のプラカード表記を英語表記の『JAPAN』としているが、1912年の初参加となったストックホルムオリンピックの選手団のみ『NIPPON』の表記を使っていた。東京と大阪にある橋の名称と地名になっている日本橋は、東京(及び旧江戸)の日本橋は"にほんばし"、大阪の日本橋は"にっぽんばし"とそれぞれ読む。日本の政党名における読みは、次のとおり（国会に複数の議席を有したことのある政党）。'
			elif city_name in '高野':
				text = ':kono_yobu_toki_sennyou_special:ほう、この私を見つけるとはやるな:kono_yobu_toki_sennyou_special:'
			else:
				text = '\''+ city_name + '\'ちょっとわからないなぁ\n関東限定、常識の範囲内でお願い！\nピンポイント検索はまた後日！'
		
		message.send(text) 