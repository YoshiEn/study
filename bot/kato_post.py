# coding: utf-8

from slacker import Slacker
import slackbot_settings

if __name__ == "__main__":
	slack = Slacker(slackbot_settings.API_TOKEN)
	slack.chat.post_message(
		'サクセスtest',
		'投手サクセスくぁっとぅ',
		username='kame',
		icon_emoji=':turtle:',
	)
	#燻製燻製燻製燻製燻製の会
	#kmbx099_亀ちゃんbot刷新対応
	#kpyx32_亀ちゃんpython刷新対応
	#general