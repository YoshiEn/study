import random

kati_count = 0;
aiko_count = 0;
make_count = 0;
sum_count = 0;
per_rireki = 0;
win_count = 0;
teki_judge = "";

class KameJanken():
	#def __init__(self):
	#	pass
	
	def jank_result(jank_judge):
		jank_name = [[1,':fist::skin-tone-3:'],[2,':v::skin-tone-3:'],[3,':raised_hand_with_fingers_splayed::skin-tone-3:'],[4,':spock-hand::skin-tone-3:'],[5,':crossed_fingers::skin-tone-3:']]
		
		ranNum = random.randrange(3);
		teki_judge = jank_name[ranNum][0]
		jank_mes = '僕とじゃんけんしょうぶだ！\nじゃんけんぽいっ！！\n' + jank_name[ranNum][1] + '\n'
		
		if teki_judge - jank_judge == 1:
			jank_mes += '負けちゃったかぁー\nこれを上げるね:50th_kunsei_passport:'
		elif jank_judge == teki_judge:
			jank_mes += 'ぐぬぬ。。。引き分けかぁ\nもう一度勝負だ！！'
		else:
			jank_mes += '君。。。じゃんけんの才能ないね。。。\nかわいそうに。。。'
		
		return jank_mes
	
	def return_kame_janken(self, message):
		global kati_count,aiko_count,make_count,sum_count,per_rireki,win_count,teki_judge
		jank_name = (message.body['text'])[5:]
		jank_judge = ''
		jank_mes = ''
		
		rock = ['ぐー', 'グー', '石', 'rock']
		scissors = ['ちょき', 'チョキ', '鋏', 'scissors']
		paper = ['ぱー', 'パー', '紙', 'paper']
		
		for i in range(4):
			if jank_name == rock[i]:
				jank_judge = 1
			elif jank_name == scissors[i]:
				jank_judge = 2
			elif jank_name == paper[i]:
				jank_judge = 3
		
		if jank_judge == '':
			jank_mes = '君はじゃんけんを知らないのかぁwwwwwwwwww\n石，鋏，紙を使おうねwwwwwwwwwwwwwwwwwwww'
		else:
			#jank_mes = jank_result
			my_select = ['( ᐛ:right-facing_fist::skin-tone-6::left-facing_fist::skin-tone-6:) グゥ','( ᐛ:v::skin-tone-6:) チョキ','( ᐛ:open_hands::skin-tone-6:) パァ']
			teki_select = [[1,':fist::skin-tone-3:'],[2,':v::skin-tone-3:'],[3,':raised_hand_with_fingers_splayed::skin-tone-3:'],[4,':spock-hand::skin-tone-3:'],[5,':crossed_fingers::skin-tone-3:']]
			
			ranNum = random.randrange(3)
			my_judge = jank_judge - 1
			teki_judge = teki_select[ranNum][0]
			result = teki_judge - jank_judge;
			jank_mes = '僕とじゃんけんしょうぶだ！じゃんけんぽいっ！！\n' + my_select[my_judge] + ' vs ' + teki_select[ranNum][1] + '\n'
			
			if result == 1 or result ==-2:
				kati_count += 1
				sum_count += 1
				jank_mes += '負けちゃったかぁー\nこれを上げるね:50th_kunsei_passport:\n'
			elif jank_judge == teki_judge:
				aiko_count += 1
				sum_count += 1
				jank_mes += 'ぐぬぬ。。。引き分けかぁ\nもう一度勝負だ！！\n'
			else:
				make_count += 1
				sum_count += 1
				jank_mes += '君。。。じゃんけんの才能ないね。。。\nかわいそうに。。。\n'
			
			jank_mes += '勝ち：' + str(kati_count) + '　引分：' + str(aiko_count) + '　負け：' + str(make_count)
			
		message.send(jank_mes)
		
		if sum_count % 10 == 0 and jank_judge != '':
			per_kati = kati_count / (kati_count + aiko_count + make_count)
			shoritu_mes = str(sum_count) + '回目だよ！\n勝率：' + str(per_kati)
			
			if per_rireki == 0:
				message.send(shoritu_mes + '\n次も頑張ろう！')
			elif per_rireki > per_kati:
				message.send(shoritu_mes + '\nえ、前回より下がってんじゃん\nきみってどうしてこんなにもだめなのかな？\nもう少し頑張りなよ？')
			else:
				win_count += 1
				tape = '';
				for i in range(win_count):
					tape += ':tukaimiti_no_nai_emozi:'
				message.send(shoritu_mes + '\nすごい！前回より上がってるね\nご褒美にいいものをあげるね！' +tape)
			
			per_rireki = per_kati