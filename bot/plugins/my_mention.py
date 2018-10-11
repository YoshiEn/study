# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from libs import my_functions           # 外部関数の読み込み
from sympy.parsing.sympy_parser import parse_expr
    
# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')      @発言者名: string でメッセージを送信
# message.send('string')       string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                              文字列中に':'はいらない
@respond_to('たこ焼き')
def mention_func(message):
    message.send('髙野が作ってくれるってよ')

@listen_to('燻製')
def listen_func(message):
	message.react('50th_kunsei_party')
	message.reply('そういえばAmaz◯Nで加藤家にスモーキングガン送ったよ！')

@listen_to('^大')
def listen_daichi(message):
	message.react('dai_chan_yobu_toki_sennyou_special')
	
@listen_to('^計算お願い')
def sympy_respond(message):
	message.reply("{} = {}".format((message.body['text'])[5:], str(parse_expr((message.body['text'])[5:]))))
