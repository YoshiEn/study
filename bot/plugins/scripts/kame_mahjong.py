import random

class KameMahjong():
	#def __init__(self):
	#	pass
	
	def return_kame_mahjong(self,message):
		Tile_Type = ['萬','索','筒','']
		Tile_Word = [['東',1],['南',2],['西',3],['北',4],['白',5],['発',6],['中',7],['',8],['',9]]
		My_Tiles = []
		for i in range(14):
			Num_T = random.randrange(4)
			Num_T = 3
			Num_N = random.randrange(126)
			Num_Div = 0
			
			if Tile_Type[Num_T] == '':
				Num_Div = 7
				Num_Jud = 0
			else:
				Num_Div = 9
				Num_Jud = 1
			
			Tile_Result = Num_N % Num_Div
			
			My_Tiles.append([Tile_Word[Tile_Result][Num_Jud],Tile_Type[Num_T]])
		
		My_Tiles.sort(key=lambda x:(x[1],x[0]))
		mah_mes = '君の手牌だよ！\n|'
		for i in range(14):
			mah_mes += str(My_Tiles[i][0]) + str(My_Tiles[i][1]) + '|'
		message.send(mah_mes)