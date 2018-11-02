# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from slacker import Slacker
import slackbot_settings
import random

from sympy.parsing.sympy_parser import parse_expr
from plugins.scripts.kame_weater import KameWeater

def_word = 'Sorry. I can\'t understand your message.';
count = 0;
countk = 0;

@respond_to('test')
def respond_func(message):
	slack = Slacker(slackbot_settings.API_TOKEN)
	channel = 'kpyx32_亀ちゃんpython刷新対応'
	slack.chat.post_message(
		channel,
		username='亀ちゃ',
		text='yaayayay',
		icon_emoji=':kamepython_move:',
	)


@listen_to('^ばいばい$')
def respond_fub(message):
	message.send('英語で「さようなら」の意。「バイバイ」として日本語化している。また挨拶を表す言葉。親しみのある者に対して用いられる。')

@listen_to('どどちゃれ')
def respond_func(message):
	ddsk = [':do:',':su:',':_ko:'];
	ddsk_num = [0,0,1,2,1,2,1,2]
	cha = [':50th_takadanobaba_cha:',':50th_kunsei_lemon_tea:',':50th_kunsei_green_cha:',':50th_kunsei_cha:']
	mes = ""
	count = 0;
	for i in range(3):
		ranNum = random.randrange(100);
		for j in range(8):
			ddsk_ran = (ddsk_num[j] + ranNum) % 3
			mes += ddsk[ddsk_ran];
		mes += '\n';
		if ddsk_ran == 2:
			count += 1;
	mes += ':sime:';
	if count == 3:
		mes += '\n君は強運だね！！これを上げよう！\n';
		mes += cha[random.randrange(len(cha))];
	message.send(mes);
	
@listen_to('ねるちゃれ')
def respond_func(message):
	neru = ['ら','り','る','れ','ろ'];
	mes = "";
	ranNum = random.randrange(5);
	for i in range(3):
		mes += 'ね' + neru[ranNum];
	mes += 'ね';
	if ranNum == 2:
		mes += '\n練れば練るほどおいしいよね:renuka_sennyou_emoji:';
	message.send(mes);

@respond_to('ごはん')
@respond_to('ご飯')
@respond_to('御飯')
def respond_func(message):
	global countk;
	text = message.body['text']
	foodlist = ""
	specialfoodlist = ['𠮷の餃子', '𠮷のｵﾑﾗｲｽ', '𠮷のﾍﾟﾍﾟﾛﾝﾁｰﾉ', '加のﾊﾟｲﾝｱﾒ', '加のﾛｰｽﾄﾋﾞｰﾌ', '坂のﾏﾝﾁｭﾘｱﾝ', '髙野塩', '大のラーメン', ':dai_chan_yobu_toki_sennyou_special:大ちゃん:dai_chan_yobu_toki_sennyou_special:']
	simplefoodlist = ['きゅうり', 'ピクルス', 'へちま', 'ズッキーニ']
	if len(text) % 2 == 0:
		foodlist = specialfoodlist
	else:
		foodlist = simplefoodlist
		
	ranNum = random.randrange(10) + random.randrange(5)
	for i in range(ranNum):
		message.reply(str(countk) +" "+ foodlist[random.randrange(len(foodlist))] + '\n')
		countk += 1;

@listen_to('僕は嫌だ！')
def listen_daichi(message):
	global count;
	if count % 2 == 1:
		message.send('亀ちゃん燻製やってもいいかな？');
	else:
		message.send('じゃあいいよ！一人で燻製するもん！');
	count += 1;
	
@listen_to('たまには燻製パーティしようかな。。。')
def listen_daichi(message):
	message.react('ore_sugoku_tanosimi_ni_siteru_yo_remake')
	message.react('ore_sugoku_tanosimi_ni_siteru_yo_remake_ver2')

@listen_to('おれ')
@listen_to('俺')
@listen_to('オレ')
def listen_func(message):
	ranNum = (random.randrange(31) + 1) % 9;
	if ranNum is 1:
		message.send('カフェオーレが飲みたいの\n強いコーヒーもいいけど\nやさしいミルクもステキなの\n白黒つけないカフェオーレ');
	elif ranNum is 2:
		message.send('I want to drink cafe au lait\nI also like strong coffee, but\nEasy milk is also nice.\nCafe au lait without black and white');
	elif ranNum is 3:
		message.send('燻製茶が飲みたいの\n強い燻製もいいけど\nやさしい燻製もステキなの\n白黒つけない燻製茶♪');
	elif ranNum is 4:
		message.send('I want to drink smoked tea\nI also like a strong smoked food, but\nEasy smoked food is also nice.\nSmoked tea without black and white');
	elif ranNum is 5:
		message.send('くっくくーんくくんくくくん\nくくんくんくんくくくくくん\nくっくくんくんくんくくっくくんくん\nくくくんくんくんくっくくーん♪');
	elif ranNum is 6:
		message.send('くんせいﾊﾟｰﾃｨがしたいの\n遠いにこたまもいいけど\nあんていのきんしちょうもすってきなの\nしろくろつけないにっしふーな♪');
	elif ranNum is 7:
		message.send('オーレオーレ　くんせいサンバ\nオーレオーレ　くんせいサンバ\nあぁ　恋せよ　スモーク\n踊ろう　ｽﾓｰｷﾝｸﾞｶﾞﾝ\n眠りさえ忘れて　燻り明かそう\nサンバ　ビバ　サンバ\nく・ん・せ・い　サンバ　オーレ');
	elif ranNum is 8:
		message.send('くーんくーん　くんせいくんく\nくーんくーん　くんせいくんく\nくー　くんせい　くんくん\nくんせい　くんくん\nくんくくんくくんく　くくくくんくん\nくんく　くく　くんく\nNI・SHI・FU・NA　くんく　くっ！');
	else:
		message.send('オーレオーレ　マツケンサンバ\nオーレオーレ　マツケンサンバ\nあぁ　恋せよ　アミーゴ\n踊ろう　セニョリータ\n眠りさえ忘れて　踊り明かそう\nサンバ　ビバ　サンバ\nマ・ツ・ケ・ン　サンバ　オーレ');

@listen_to('楽しい')
@listen_to('たのし')
@listen_to('面白')
@listen_to('おもしろ')
def listen_func(message):
	ranNum = random.randrange(4);
	forYou = ':turtle:';
	if ranNum is 0:
		kame_text = 'bot開発しようよ！'
	elif ranNum is 1:
		kame_text = 'サクセス進めようよ！'
	elif ranNum is 2:
		kame_text = 'バトル早く仕上げたいね！'
	else:
		kame_text = 'トイレで鏡を見れば、面白いもの見れるよ！'
	message.send(kame_text)

@listen_to('眠い')
@listen_to('眠そ')
@listen_to('ねむい')
def listen_func(message):
	ranNum = random.randrange(5)
	forYou = ':turtle:';
	if ranNum is 0:
		forYou = ':for_igari_san:' + forYou
	elif ranNum is 1:
		forYou = ':for_kato:' + forYou
	elif ranNum is 2:
		forYou = ':forkono_part4:' + forYou
	elif ranNum is 4:
		forYou = '\n…とでも言うとおもったか？\n働けゴミクズ！！！'
	else:
		forYou = ':50th_kunsei_cha:' + forYou
	message.send('大丈夫！？これで元気出して！' + forYou)

@listen_to('燻製茶')
def listen_func(message):
	message.react('yoshisan_tte_shitai_hito_sennyou')
	message.react('nanika_you_ka_hatena')
	message.react('saka_san_yobitai_toki_sennyou')
	message.react('yasei_no_unknow_ga_arawareta')
	message.react('interrobang')
	message.react('a_akogareno_pokemon_master_ni_naritaina_naranakutya_zettai_natteyaru')
	message.react('boom')
	if random.randrange(2) == 1:
		message.react('pokemon_get_daze')
		message.react('hugging_face')
	else:
		message.react('項目追加撃退用絵文字')

@listen_to('^ダイ')
@listen_to('大ちゃん')
@listen_to('大地')
def listen_daichi(message):
	message.react('dai_chan_yobu_toki_sennyou_special')

@listen_to('𠮷')
def listen_daichi(message):
	message.react('yoshi_san_yobu_toki_sennyou_special')

@listen_to('^加藤')
@listen_to('^聡')
@listen_to('さと')
def listen_daichi(message):
	message.react('satoshi_yobu_toki_sennyou_special')

@listen_to('髙')
def listen_daichi(message):
	message.react('kono_yobu_toki_sennyou_special')

@listen_to('坂')
def listen_daichi(message):
	message.react('saka_san_yobu_toki_sennyou_special')

@listen_to('高野')
def listen_kono(message):
	message.reply('高野じゃなくて髙野だってば！')

@listen_to('^_help$')
def kame_respond(message):
	message.send('\n_command ◯◯◯ でkameちゃん便利機能が使えます！')
	message.send('\n_set: バイリンガルの如く、kameちゃんのデフォルト語が変わります。\n_math: 関数電卓の如く、計算してくれます。\n_weather: 気象庁の如く、天気を教えてくれます。※日本は絶対に調べないでください！\n_task: 燻製の如く、加藤の予定を教えてくれます。')
		
@listen_to('^_math\s+\S.*')
def kame_respond(message):
	try:
		message.reply("{} = {}".format((message.body['text'])[5:], str(parse_expr((message.body['text'])[5:]))))
	except:
		message.reply('半角英数字の数式じゃないと分かんないよ。。。');

@listen_to('^_set\s+\S.*')
def kame_respond(message):
	text = message.body['text']     # メッセージを取り出す
	temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'set'が入る
	global def_word     # 外で定義した変数の値を変えられるようにする
	def_word = word     # デフォルトの返事を上書きする
	msg = 'デフォルトの返事を以下のように変更しました。\n```' + word + '```'
	message.react('ryo')
	message.send(msg)

@listen_to('^_weather\s+\S.*')
def weather(message):
	weather_class = KameWeater()
	weather_class.return_kame_weater(message)
@listen_to ('^_task$')
def kame_respond(message):
	message.send('加藤ちゃんがやるべきことをまとめたよ！')
	message.send('\n 亀ちゃんDB')
	message.send('\n 燻製企画作成(内部レビュー：髙野，坂/外部レビュー：遠藤，遠藤)')
	message.send('\n パインアメ補給')

@default_reply()
def kame_def_respond(message):
	message.reply(def_word)     # def_wordの文字列を返す