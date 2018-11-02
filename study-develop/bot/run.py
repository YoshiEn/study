# coding: utf-8

from slackbot.bot import Bot
from slacker import Slacker
import slackbot_settings
from datetime import datetime


def main():
	bot = Bot()
	bot.run()
	
# kmbx099_亀ちゃんbot刷新対応
# kpyx32_亀ちゃんpython刷新対応
if __name__ == "__main__":
	print('start slackbot')
	channel = 'kpyx32_亀ちゃんpython刷新対応'
	slack = Slacker(slackbot_settings.API_TOKEN)
	nowhour = datetime.now().hour
	if nowhour < 8 or nowhour > 18:
		message = '業務外なのに頑張るね！\nよっ！社畜の鑑！:for_igari_san:'
		channel = 'kpyx32_亀ちゃんpython刷新対応'
	elif nowhour < 9 or nowhour > 17:
		message = '業務外なのに頑張るね！\nよっ！社畜の鑑！:for_igari_san:'
	elif nowhour < 11:
		message = 'おはようございます。'
	elif nowhour < 16:
		message = 'こんにちは。'
	else:
		message = 'こんばんは。'
	spemessage = ''
	slack.chat.post_message(
		channel,
		'…亀ちゃん(ver py)が起動いたしました。\n' + message + spemessage,
		username='亀ちゃん(ver py)',
		icon_emoji=':kamepython_move:',
	)
	main()