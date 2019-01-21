# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from slacker import Slacker
import slackbot_settings
import random
import time
import re

from sympy.parsing.sympy_parser import parse_expr
from plugins.scripts.kame_weater import KameWeater
from plugins.scripts.kame_janken import KameJanken
from plugins.scripts.kame_mahjong import KameMahjong

def_word = 'Sorry. I can\'t understand your message.';
count = 0;
countk = 0;
counta = 0;
c_list = [0,0,0,0,0,0]
kati_count = 0;
aiko_count = 0;
make_count = 0;
kono_flg = 0;


new_job = ['ksc','scii']
id_all = ['U8HSAK31R','UED0YUVK7','U8J9BHS74','U8J39648M','U8JQFANUW','UA31WJ8VA']
id_spe = ['U8HSAK31R','UED0YUVK7','U8J9BHS74','U8J39648M','U8JQFANUW']
today_list = random.sample(id_all,6)
today_list = random.sample(today_list,6)
today_list = random.sample(today_list,6)
game21 = 0;
game21_num = 21
lFlg = 0
count_hasuu = (4 - (game21_num + 3) % 4) % 4

@respond_to('test1')
def respond_func(message):
	slack = Slacker(slackbot_settings.API_TOKEN)
	channel = 'general'
	slack.chat.post_message(
		channel,
		username='加藤聡',
		text='月末燻製パーティやります！',
		icon_emoji=':satoshi_yobu_toki_sennyou_special:',
	)

@respond_to('test2')
def respond_func(message):
	slack = Slacker(slackbot_settings.API_TOKEN)
	channel_id = 'kpyx32_亀ちゃんpython刷新対応'
	channel_id = slack.channels.get_channel_id('kpyx32_亀ちゃんpython刷新対応')
	slack.chat.command(
			channel=channel_id,
			command='/poll',
			text='"Do you prefer cats or dogs?" "Cats" "Dogs"'
	)

@respond_to('髙野翔生')
@listen_to('おれ')
@listen_to('俺の')
@listen_to('オレ')
def respond_func(message):
	global kono_flg, id_all
	message.react('ryo')
	kono_flg = abs(kono_flg - 1)
	
	if kono_flg == 0:
		mes = '罵るスイッチがOFFになりました。'
		if  message.body['user'] == id_all[0]:
			user = '𠮷さんの頼みなら断れないなぁ！'
		elif message.body['user'] == id_all[1]:
			user = ''
			mes = 'いや、君がスイッチ切れるわけないでしょ？ｗ\n誰かに土下座して切ってもらったら？ｗｗｗ'
			kono_flg += 1
		elif message.body['user'] == id_all[2]:
			user = 'さ、さ、、さ、、、さかさｎ！！'
		elif message.body['user'] == id_all[3]:
			user = 'だいちゃーーーーーん！'
		elif message.body['user'] == id_all[4]:
			user = 'そろそろ燻製パーティしないの？'
		elif message.body['user'] == id_all[5]:
			user = 'うあぁぁぁあ～～～～～～～～～～～～'
		else:
			user = '(´；ω；｀)ﾌﾞﾜｯ'
	else:
		mes = '罵るスイッチがONになりました。'
		user = ''
	message.send(user + mes)
	
	

@listen_to('')
def respond_iyagarase(message):
	global kono_flg, c_list, id_all
	
	if kono_flg == 1:
		message.send('<@' + id_all[1] + '> ボっコこ')
	
	try:
		uName = message.body['user']
		for i in range(len(id_all)):
			if uName == id_all[i]:
				c_list[i] += 1
	except:
		pass

@respond_to('結果発表！')
def respond_iyagarase(message):
	global c_list, id_all
	numbox = c_list[0]
	namebox = '<@' + id_all[0] + '>'
	for i in range(1,len(c_list)):
		if numbox < c_list[i]:
			numbox = c_list[i]
			namebox = '<@' + id_all[i] + '>さん' 
		elif numbox	 == c_list[i]:
			namebox += '<@' + id_all[i] + '>さん'
	message.send('本日一番うるさかった人は' + namebox + 'でした！')

@listen_to('うん')
def respond_iyagarase(message):
	message.send('<@' + id_all[1] + '> うん、こーの')

@listen_to('明日の天気:')
def respond_func(message):
	global today_list
	slack = Slacker(slackbot_settings.API_TOKEN)
	channel = 'general'
	mes = '明日の運勢です。\n'
	for i in range(len(today_list)):
		mes += '　' + str(i + 1) + '位： <@' + today_list[i] + '>\n'
	mes += '明日も一日がんばろう！'
	slack.chat.post_message(
		channel,
		username='占い師',
		text=mes,
		icon_emoji=':self_double_check_niha_gochui_wo_:',
	)

@listen_to('燻製した')
@listen_to('つんでれ')
@listen_to('ツンデレ')
def respond_func(message):
	slack = Slacker(slackbot_settings.API_TOKEN)
	channel = '亀ちゃんbotなんちゃら'
	slack.chat.post_message(
		channel,
		username='加藤聡',
		text='俺だ俺だ俺だ俺だ俺だ俺だ俺だ俺だ俺だ俺だ！',
		icon_emoji=':satoshi_yobu_toki_sennyou_special:',
	)

@listen_to('^ばいばい$')
def respond_fub(message):
	message.reply('英語で「さようなら」の意。「バイバイ」として日本語化している。また挨拶を表す言葉。親しみのある者に対して用いられる。')

@respond_to('くんせいこと')
def respond_func(message):
	message.send('たまご燻って 君（黄身）を愛せるか？');
	time.sleep(5);
	message.send('本当に君（黄身）を 守れるか？');
	time.sleep(5);
	message.send('煙見て 考えてた');
	time.sleep(6);
	message.send('君（黄身）のために 今何を燻すか');
	time.sleep(6);
	message.send('忘れないでどんな時も');
	time.sleep(5);
	message.send('きっとたまごあるから');
	time.sleep(5);
	message.send('そのために僕らは にしふなで');
	time.sleep(5);
	message.send('同じ煙をあびて 同じたまご食べるんだ');

@respond_to('燻唄')
def respond_func(message):
	message.send('「ねぇ、大好きな君（黄身）へ」 煮込まないで聞いてくれ');
	time.sleep(6);
	message.send('「燻ってる」だなんて臭いけどね');
	time.sleep(5.5);
	message.send('だけど、この調理法しか 伝えることができない');
	time.sleep(6);
	message.send('ほらね！またバカにして煮込んだよね！？');
	time.sleep(5.5);
	message.send('君の選んだ燻製（ミチ）は加藤家（ココ）で良かったのか？なんて');
	time.sleep(10.5);
	message.send('分からないけど、、、');
	time.sleep(3);
	message.send('ただ 燻って 煙（けむ）って 過ごす日々に');
	time.sleep(6);
	message.send('隣に立って 燻れることでー↑ー↓');
	time.sleep(5.5);
	message.send('僕を燻る 意味になって');
	time.sleep(6);
	message.send('黄身に捧ぐ この燻の唄');

@respond_to('燻の歌')
def respond_func(message):
	message.send('燻製されてあなただけに食べられる');
	time.sleep(4);
	message.send('今日も燻す燻す燻す');
	time.sleep(2);
	message.send('そして');
	time.sleep(1);
	message.send('食べられる');
	time.sleep(2);
	message.send('ほったかされて、またあって、煙たがれて');
	time.sleep(4);
	message.send('でも私たちあなたに燻され尽くします');

@respond_to('燻製の歌')
def respond_func(message):
	global id_all
	userid = '<@' + id_all[random.randrange(5)] + '> '
	message.send(userid + 'だ、だだだだいちゃーんだだだーいちゃんだだーいちゃーん♡');
	time.sleep(4);
	userid = '<@' + id_all[random.randrange(5)] + '> '
	message.send(userid + 'だーいーだいちゃんだいちゃんだいちゃん♡');
	time.sleep(2);
	userid = '<@' + id_all[random.randrange(5)] + '> '
	message.send(userid + 'だいちゃん♡');
	time.sleep(1);
	userid = '<@' + id_all[random.randrange(5)] + '> '
	message.send(userid + 'だいーだいちゃん♡');
	time.sleep(2);
	userid = '<@' + id_all[random.randrange(5)] + '> '
	message.send(userid + 'だっだだだーいちゃん、だいちゃーん、だいだいちゃーん♡');
	time.sleep(4);
	userid = '<@' + id_all[random.randrange(5)] + '> '
	message.send(userid + 'だいちゃんだーいちゃーんだいだいだいちゃんだいーだいちゃん♡');

	
@respond_to('WAVE')
def respond_func(message):
	message.send('Oh西よ 西船橋よ');
	time.sleep(4);
	message.send('掴め夢と燻製の日々よ');
	time.sleep(4);
	message.send('この先も変わらぬ愛と Smokingで。。。');
	time.sleep(5);
	message.send('うをぅうをぅうをぅ！うをぅうをぅうをぅ！');
	time.sleep(3);
	message.send('燻せ くーんくーんくん↓くーんくーんくん↑くーんくーん↑くーんくん→');
	time.sleep(3);
	message.send('くーんくーんくん↓くーんくーんくん↑くーんくーん↑くーんくん→');
	time.sleep(3);
	message.send('くーんくーんくん↓くーんくーんくん↑くーんくーん↑くーんくん→');
	time.sleep(3);
	message.send('行くぜ 燻製から西船の果てまで');
	time.sleep(3);
	message.send('燻せ くーんくーんくん↓くーんくーんくん↑くーんくーん↑くーんくん→');
	time.sleep(3);
	message.send('てーめぇ↓なりぃの↑くんせい↑みせぃ→');
	time.sleep(3);
	message.send('くーんくーんくん↓くーんくーんくん↑くーんくーん↑くーんくん→');
	time.sleep(3);
	message.send('行くぜ 不可能はねぇ 燻せ夢');
	message.send(':kan:');

@respond_to('燻製歌')
def respond_func(message):
	message.send('目を閉じれば　燻製の星');
	time.sleep(3);
	message.send('一番ヒカル 聡がいる');
	time.sleep(3);
	message.send('はじめてベーコンになったよぉうぉ');
	time.sleep(3);
	message.send('夜空へ届け燻製玉');
	time.sleep(5);
	message.send('くーんくくくーんくくーくーんくくーんくくくくーんくくんくんー');
	time.sleep(5);
	message.send('くーんくくくーんくくーくーんくくーんくくくくーんくくんくんー');
	for i in range(5):
		ranNum1 = random.randrange(5)
		ranNum2 = random.randrange(5)
		ranNum3 = random.randrange(5)
		ranNum4 = random.randrange(4)
		if ranNum1 == 0:
			omaename1 = ':satoshi_yobu_toki_sennyou_special:'
		elif ranNum1 == 1:
			omaename1 = ':yoshi_san_yobu_toki_sennyou_special:'
		elif ranNum1 == 2:
			omaename1 = ':saka_san_yobu_toki_sennyou_special:'
		elif ranNum1 == 3:
			omaename1 = ':dai_chan_yobu_toki_sennyou_special:'
		else:
			omaename = ':barber_kono:'
		if ranNum2 == 0:
			omaename2 = ':satoshi_yobu_toki_sennyou_special:'
		elif ranNum2 == 1:
			omaename2 = ':yoshi_san_yobu_toki_sennyou_special:'
		elif ranNum2 == 2:
			omaename2 = ':saka_san_yobu_toki_sennyou_special:'
		elif ranNum2 == 3:
			omaename2 = ':dai_chan_yobu_toki_sennyou_special:'
		else:
			omaename2 = ':barber_kono:'
		if ranNum3 == 0:
			omaename3 = ':satoshi_yobu_toki_sennyou_special:'
		elif ranNum3 == 1:
			omaename3 = ':yoshi_san_yobu_toki_sennyou_special:'
		elif ranNum3 == 2:
			omaename3 = ':saka_san_yobu_toki_sennyou_special:'
		elif ranNum3 == 3:
			omaename3 = ':dai_chan_yobu_toki_sennyou_special:'
		else:
			omaename = ':barber_kono:'
		message.send('大親友('+omaename1+')の彼女の'+omaename2+' おいしいパスタ作った'+omaename3);
		time.sleep(ranNum4)

@respond_to('燻製花')
def respond_func(message):
	message.send('燻製の花のように…');
	time.sleep(3);
	message.send('朝日に向け今日も燻す…');
	time.sleep(2);
	message.send('燻製の花のように…');
	time.sleep(3);
	message.send('この思い煙にヒカル…');
	time.sleep(2);
	message.send('目に煙で流した涙　あなたは笑えていますか');
	time.sleep(3);
	message.send('上がりまくる季節が来た　燻製したくなるのは誰………');
	time.sleep(5);
	#message.send('※ただいま加藤聡様は喉を壊しております。※\n※治療中ですので今しばらくお待ちください。※');
	
	slack = Slacker(slackbot_settings.API_TOKEN)
	channel = '亀ちゃんbotなんちゃら'
	for i in range(5):
		ranNum1 = random.randrange(5)
		ranNum2 = random.randrange(2)
		ranNum3 = random.randrange(4)
		if ranNum1 == 0:
			username = '加藤聡'
			if ranNum2 == 0:
				text = '俺だ俺だ俺だ俺だ俺だ俺だ俺だ俺だ俺だ俺だ！'
			else:
				text = '燻製燻製燻製燻製燻製燻製燻製燻製燻製！'
			icon_emoji = ':satoshi_yobu_toki_sennyou_special:'
		elif ranNum1 == 1:
			username = '遠藤𠮷和'
			if ranNum2 == 0:
				text = 'ｻｶｻﾝ！ｻｶｻﾝ！ｻｶｻﾝ！ｻｶｻﾝ！ｻｶｻﾝ！ｻｶｻﾝ！'
			else:
				text = '誰かと思えばｻｶｻﾝじゃないか。。。'
			icon_emoji = ':yoshi_san_yobu_toki_sennyou_special:'
		elif ranNum1 == 2:
			username = '坂翔汰郎'
			if ranNum2 == 0:
				text = 'ﾖｼｻﾝ！ﾖｼｻﾝ！ﾖｼｻﾝ！ﾖｼｻﾝ！ﾖｼｻﾝ！ﾖｼｻﾝ！'
			else:
				text = 'ま、、ま、、ま、、、、まんちゅりあぁぁん！！'
			icon_emoji = ':saka_san_yobu_toki_sennyou_special:'
		elif ranNum1 == 3:
			username = '遠藤大地'
			if ranNum2 == 0:
				text = '安心してください。はいて…ませんでした！'
			else:
				text = '安心してください。はいてますよ？'
			icon_emoji = ':dai_chan_yobu_toki_sennyou_special:'
		else:
			username='髙野翔生'
			if ranNum2  == 0:
				text = '最近ちょっとずつ縮んでんだぞ！'
			else:
				text = '《特集１》\n要件定義はもうやらない\n\n《特集２》\nリーダーを困らせる厄介な部下'
			icon_emoji = ':barber_kono:'
		
		slack.chat.post_message(
			channel,
			username = username,
			text = text,
			icon_emoji = icon_emoji,
		)
		time.sleep(ranNum3)
	
@listen_to('どどちゃれ')
def respond_func(message):
	ddsk = [':do:',':su:',':_ko:'];
	ddsk_num = [0,0,1,2,1,2,1,2]
	cha = [':50th_takadanobaba_cha:',':50th_kunsei_lemon_tea:',':50th_kunsei_green_cha:',':50th_kunsei_cha:',':50th_kunsei_cha:',':50th_kunsei_passport:']
	mes = ""
	count = 0;
	text = message.body['text']     # メッセージを取り出す
	word = text[5:9]
	if word == "かんたん" or word == "イージー" or word == "いーじー" or word == "easy":
		Num1 = 1;
	elif word == "むずかし" or word[:3] == "はーど" or word[:3] == "ハード" or word == "hard":
		Num1 = 3;
	else:
		Num1 = 99;
	
	for i in range(3):
		ranNum = random.randrange(Num1);
		if Num1 == 3:
			for k in range(len(ddsk_num)):
				ddsk_num[k] = random.randrange(Num1);
		
		for j in range(8):
			ddsk_ran = (ddsk_num[j] + ranNum) % 3
			mes += ddsk[ddsk_ran];
		message.send(mes);
		mes = "";
		
		if ddsk_ran == 2:
			count += 1;
		
		time.sleep(1);
	
	message.send(':sime:');
	time.sleep(0.5);
	if count == 3:
		mes = cha[random.randrange(len(cha))];
	else:
		mes = ':kan_s_rival:';
	message.send(mes);
	
@respond_to('カウント初期化')
def respond_func(message):
	global countk;
	countk = 0;
	message.send('カウントが正常に初期化されました')

@respond_to('ごはん')
@respond_to('ご飯')
@respond_to('御飯')
@respond_to('\+:+1:')
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
		if countk > 20:
			message.reply("加藤の家で燻製パーティ開催決定！\n")
		elif countk > 12:
			message.reply("腐った"+ foodlist[random.randrange(len(foodlist))] + '\n')
		elif countk > 10:
			message.reply("燻製した"+ foodlist[random.randrange(len(foodlist))] + '\n')
		elif countk > 5:
			message.reply("乾燥させた"+ foodlist[random.randrange(len(foodlist))] + '\n')
		else:
			message.reply(foodlist[random.randrange(len(foodlist))] + '\n')
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
	time.sleep(10)
	message.react('so')
	time.sleep(0.3)
	message.react('-')
	time.sleep(0.3)
	message.react('da')
	time.sleep(0.3)
	message.react('wash_your_face')
	time.sleep(0.3)
	message.react('satoshi_skiing_bu_from_konosu_si')
	time.sleep(0.3)
	message.react('house')
	time.sleep(0.3)
	message.react('50th_kunsei_party')
	time.sleep(0.3)
	message.react('e')
	time.sleep(0.3)
	message.react('ko')
	time.sleep(0.3)
	message.react('ka')
	time.sleep(0.3)
	message.react('space_you_ni_douzo')
	time.sleep(0.3)
	message.react('igo_mukou_to_simasu')

'''
def listen_func(message):
	ranNum = (random.randrange(31) + 1) % 12;
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
	elif ranNum is 9:
		message.send('オーレオーレ　マツケンサンバ\nオーレオーレ　マツケンサンバ\nあぁ　恋せよ　アミーゴ\n踊ろう　セニョリータ\n眠りさえ忘れて　踊り明かそう\nサンバ　ビバ　サンバ\nマ・ツ・ケ・ン　サンバ　オーレ');
	elif ranNum is 10:
		message.send('This lid of this kid\'s head this kid ♪\nI caught it from the downstream of Tama ♪\nThis shrinking of this fucking ♪\nWeight loss woman nostalgia ♪');
	else:
		message.send('そうだ うれしいんだ 燻す よろこび\nたとえ へやの におい しみついても\nああ カトウサトシ  やさしい きみは\nいけ！ くんせい ﾊﾟｰﾃｨ ひらくため');
'''
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
	global id_all
	userid = '<@' + id_all[4] + '> '
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
@listen_to('GAS')
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
	message.react('saka_san_yobu_toki_sennyou_kikan_gentei')
	message.react('saka_san_yobu_toki_sennyou_special')

@listen_to('高野')
def listen_kono(message):
	message.reply('高野じゃなくて髙野だってば！')

@listen_to('^_help$')
def kame_respond(message):
	message.send('\n_command ◯◯◯ でkameちゃん便利機能が使えます！\n今歌える曲: 睡蓮花、純恋歌、WAVE、燻のうた（作詞daichan）、燻製の歌（？？？？？）')
	message.send('\n_set: バイリンガルの如く、kameちゃんのデフォルト語が変わります。\n_math: 関数電卓の如く、計算してくれます。\n_weather: 気象庁の如く、天気を教えてくれます。※日本は絶対に調べないでください！\n_task: 燻製の如く、加藤の予定を教えてくれます。\n_rps: 幼稚園の先生の如く、じゃんけんの相手をしてくれます。\n_newjob: エージェントの如く、新しいジョブを追加してくれます。\n_alljob: エージェントの如く、仕事を教えてくれます。')
		
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
	message.send('\n 燻製パーティ')
	message.send('\n 燻製パーティ')
	message.send('\n 燻製パーティ')
	message.send('\n 燻製パーティ')
	message.send('\n 亀ちゃんDB')
	message.send('\n 燻製企画作成(内部レビュー：髙野，坂/外部レビュー：遠藤，遠藤)')
	message.send('\n パインアメ補給')

@listen_to ('^_rps\s+\S.*')
def kame_respond(message):
	janken_class = KameJanken()
	janken_class.return_kame_janken(message)

@listen_to ('^_test$')
def kame_respond(message):
	mahjong_class = KameMahjong()
	payload = {'icon_emoji': ':dog:'}
	mahjong_class.return_kame_mahjong(message)


@listen_to ('^_newjob\s+\S.*')
def kame_respond(message):
	global new_job
	wordflg = 0;
	
	text = message.body['text']     # メッセージを取り出す
	word = text[8:]
	for i in range(len(new_job)):
		if word == new_job[i]:
			wordflg = 1;
	
	if wordflg == 0:
		message.react('ryo')
		new_job.append(word)
		message.send( "職業名「" + word + "」を追加しました！")
	else:
		message.react('x')
		message.send('その職業は登録されているよ！')

@listen_to ('^_alljob$')
def kame_respond(message):
	global new_job
	mes = "今ある職業だよ！"
	
	for i in range(len(new_job)):
		if i % 5 == 0:
			mes += "\n"
		else:
			mes += " / "
		mes += new_job[i]
	message.send(mes)

@listen_to ('^_himagame\s+\S.*')
def kame_respond(message):
	global game21,game21_num,lFlg,count_hasuu
	eFlg = 0
	count = 0
	nBox = int(game21)
	
	text = message.body['text']     # メッセージを取り出す
	word = text[10:]
	
	if word.replace(',','').isdecimal():
		word = word.split(',')
		if len(word) < 4:
			for i in range(len(word)):
				number = int(word[i])
				if number == game21_num and lFlg != 2:
					eFlg = 1
					lFlg = 1
				if nBox == number - 1 and eFlg == 0:
					nBox = number
				else:
					eFlg = 1
		else:
			eFlg = 1
		if lFlg == 2:
				mes = 'うわぁあああぁあ！\n:goro_goro_site_miso::goro_goro_site_miso::goro_goro_site_miso:\n:goro_goro_site_miso::kamepython::goro_goro_site_miso:\n:goro_goro_site_miso::goro_goro_site_miso::goro_goro_site_miso:'
		elif eFlg == 0:
			count = 4 - ((nBox + count_hasuu) % 4)
			if count == 4:
				count = random.randrange(3) + 1
			nBox += 1
			mes = 'これでどうだ！ ' + str(nBox)
			if nBox == game21_num:
				lFlg ==2
			
			for i in range(count-1):
				if nBox != game21_num:
					nBox += 1
					mes += ',' + str(nBox)
				else:
					lFlg = 2
			
			if lFlg == 2:
				mes += '\nうわぁあああぁあ！\n:boom::boom::boom:\n:boom::kamepython::boom:\n:boom::boom::boom:'
			game21 = nBox
		elif lFlg == 1:
			mes = '君の負けだよ！初期化はclearと打ってね！'
		else:
			if len(word) < 4:
				mes = 'ちゃんとやってよ！次の数字は' + str(game21+1) + 'だよ！'
			else:
				mes = '4つ以上はだめだよ！次の数字は' + str(game21+1) + 'だよ！'
	elif word == 'clear':
		lFlg = 0
		game21 = 0
		game21_num = random.randrange(15) + 8
		count_hasuu = (4 - (game21_num + 3) % 4) % 4
		mes = '初期化しました。僕に勝てるかな？'
		mes += '\n次は' + str(game21_num) + 'で勝負だ！'
	else:
		mes = 'ERR' + str(type(word))
	
	
	message.send(mes)

@listen_to ('転職')
def kame_respond(message):
	global new_job
	ranNum = random.randrange(len(new_job))
	mes = "転職先は「" + new_job[ranNum] + "」だよ！やったね！"
	message.reply(mes)

@default_reply()
def kame_def_respond(message):
	message.reply(def_word)     # def_wordの文字列を返す