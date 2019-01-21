# coding: utf-8

from slacker import Slacker
import slackbot_settings

if __name__ == "__main__":
	slack = Slacker(slackbot_settings.API_TOKEN)
	
	slack.chat.post_message(
		'amazon部屋',
		'げんきしとぉや！！',
		username='栃本仁',
		icon_emoji=':goro_goro_site_miso:',
	)
	slack.chat.post_message(
		'java部屋',
		'げんきしとぉや！！',
		username='栃本仁',
		icon_emoji=':goro_goro_site_miso:',
	)
	slack.chat.post_message(
		'python部屋',
		'げんきしとぉや！！',
		username='栃本仁',
		icon_emoji=':goro_goro_site_miso:',
	)
	#燻製燻製燻製燻製燻製の会
	#kmbx099_亀ちゃんbot刷新対応
	#kpyx32_亀ちゃんpython刷新対応
	#general
"""	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		'坂ちゃんだよぉぉぉぉぉっぉぉぉぉぉぉぉぉぉぉぉおぉぉぉ！',
		username='坂ちゃん',
		icon_emoji=':saka_san_yobu_toki_sennyou_kikan_gentei:',
	)
	slack.chat.post_message(
		'第1回たこやきパーティーやっても委員会',
		'げんきしとぉや！！',
		username='栃本仁',
		icon_emoji=':goro_goro_site_miso:',
	)
	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		'𠮷ちゃんだよぉぉぉぉぉっぉぉぉぉぉぉぉぉぉぉぉおぉぉぉ！',
		username='𠮷ちゃん',
		icon_emoji=':yoshi_san_yobu_toki_sennyou_kibun_ga_yoi_toki:',
	)
	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		'大ちゃんだよぉぉぉぉぉっぉぉぉぉぉぉぉぉぉぉぉおぉぉぉ！',
		username='大ちゃん',
		icon_emoji=':dai_chan_yobu_toki_sennyou_special_o_ma_ta_se:',
	)
	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		'さとちゃんだよぉぉぉぉぉっぉぉぉぉぉぉぉぉぉぉぉおぉぉぉ！',
		username='さとちゃん',
		icon_emoji=':satoshi_yobu_toki_sennyou_special_hi_tension:',
	)
	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		"We are the smoked meat, we are the smoked fish\nWe are the ones who make a smoking day\nSo let's start smoking\nThere's a choice we're smoking\nWe're smoking our own smokes　\nIts true well smoke a better day\nJust you and me",
		username='高野ちゃん',
		icon_emoji=':barber_kono:',
	)
"""