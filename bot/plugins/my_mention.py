# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from sympy.parsing.sympy_parser import parse_expr
#from libs import my_functions           # 外部関数の読み込み
from plugins.scripts.kame_weater import KameWeater

def_word = 'Sorry. I can\'t understand your message.'

@respond_to('ごはん')
@respond_to('ご飯')
@respond_to('御飯')
def respond_gohan(message):
	import random
	ranNum = random.randrange(10) + 1
	for i in range(ranNum):
		message.reply('きゅうり\n')

@listen_to('眠い')
@listen_to('眠そ')
@listen_to('ねむい')
def listen_func(message):
	import random
	ranNum = random.randrange(4)
	forYou = ':turtle:';
	if ranNum is 0:
		forYou = ':for_igari_san:' + forYou
	elif ranNum is 1:
		forYou = ':for_kato:' + forYou
	elif ranNum is 2:
		forYou = ':forkono_part4:' + forYou
	else:
		forYou = ':50th_kunsei_cha:' + forYou
	message.send('大丈夫！？これで元気出して！' + forYou)


@listen_to('燻製茶')
@listen_to('亀ちゃん')
def listen_func(message):
	import random
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

@listen_to('高野')
def listen_kono(message):
	message.reply('高野じゃなくて髙野だってば！')

@listen_to('^_help$')
def kame_respond(message):
	message.send('\n_command ◯◯◯ でkameちゃん便利機能が使えます！')
	message.send('\n_set: バイリンガルの如く、kameちゃんのデフォルト語が変わります。\n_math: 関数電卓の如く、計算してくれます。\n_weather: 気象庁の如く、天気を教えてくれます。※日本は絶対に調べないでください！')
		
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

@default_reply()
def kame_def_respond(message):
	message.reply(def_word)     # def_wordの文字列を返す

# twitter から持ってこれるようにしたいね
# from service import twitter_service

# @respond_to('collectTweet (.*)')
# def collect_user_tweet(message, word):
# twitter_service.collect_user_tweet(word)
