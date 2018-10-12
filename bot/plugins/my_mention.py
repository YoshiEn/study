# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from sympy.parsing.sympy_parser import parse_expr
#from libs import my_functions           # 外部関数の読み込み

def_word = 'うるせぇな'

@respond_to('たこ焼き')
def mention_func(message):
    message.send('髙野が作ってくれるってよ')

@listen_to('燻製茶')
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
	else:
		message.react('項目追加撃退用絵文字')
		
@listen_to('^大')
@listen_to('^ダイ')
@listen_to('大ちゃん')
@listen_to('大地')
def listen_daichi(message):
	message.react('dai_chan_yobu_toki_sennyou_special')

@listen_to('21')
def listen_attack(message):
	message.react('gyakuten_no_chance_ga_arukamo_ne')
	message.react('dai_chan_yobu_toki_sennyou_special')
	message.react('su')

@listen_to('^坂さん')
def listen_sakasan(message):
	message.react('nanika_you_ka_hatena')
	message.react('yoshisan_tte_shitai_hito_sennyou')

@listen_to('^𠮷さん')
def listen_yoshisan(message):
	message.react('nanika_you_ka_hatena')
	message.react('saka_san_yobitai_toki_sennyou')

@listen_to('^加藤')
def listen_satoshi(message):
	message.react('i_love_you_hand_sign')
	message.react('ka_to_no_roast_beef')

@listen_to('^髙野')
def listen_kono(message):
	message.react('space_you_ni_douzo')

@listen_to('^高野')
def listen_kono(message):
	message.reply('高じゃなくて髙だってば！')
	
@listen_to('^_math')
def sympy_respond(message):
	try:
		message.reply("{} = {}".format((message.body['text'])[5:], str(parse_expr((message.body['text'])[5:]))))
	except:
		message.reply('半角英数字の数式じゃないと分かんないよ。。。');

@default_reply()
def default_func(message):
	message.reply(def_word)     # def_wordの文字列を返す

@listen_to('^_set\s+\S.*')
def set_default_func(message):
	text = message.body['text']     # メッセージを取り出す
	temp, word = text.split(None, 1)    # 設定する言葉を取り出す。tempには'set'が入る
	global def_word     # 外で定義した変数の値を変えられるようにする
	def_word = word     # デフォルトの返事を上書きする
	msg = 'デフォルトの返事を以下のように変更しました。\n```' + word + '```'
	message.react('ryo')
	message.send(msg)
	
# twitter から持ってこれるようにしたいね
# from service import twitter_service

# @respond_to('collectTweet (.*)')
# def collect_user_tweet(message, word):
    # twitter_service.collect_user_tweet(word)