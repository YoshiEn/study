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
	slack = Slacker(slackbot_settings.API_TOKEN)
	nowhour = datetime.now().hour
	if nowhour < 9 or nowhour > 18:
		message = '業務外なのに頑張るね！\nよっ！社畜の鑑！:for_igari_san:'
	elif nowhour < 11:
		message = 'おはようございます。'
	elif nowhour < 16:
		message = 'こんにちは。'
	else:
		message = 'こんばんは。'
	slack.chat.post_message(
		'kmbx099_亀ちゃんbot刷新対応',
		'亀ちゃん(ver py)が起動いたしました。\n' + message,
		username='亀ちゃん(ver py)',
		icon_emoji=':kamepython:',
	)
	main()	#if datetime.now().hour
