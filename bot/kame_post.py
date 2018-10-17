# coding: utf-8

from slacker import Slacker
import slackbot_settings

if __name__ == "__main__":
	slack = Slacker(slackbot_settings.API_TOKEN)
	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		'KSCの髙野です。',
		username='しょうき',
		icon_emoji=':kono_yobu_toki_sennyou_special:',
	)
	#kpyx32_亀ちゃんpython刷新対応