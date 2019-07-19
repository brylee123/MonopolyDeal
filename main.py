#import init_deck
import init_players
import draw_util

if __name__ == '__main__':
	#game_deck = init_deck.shuffle_deck()
	game_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	
	print("Welcome to Monopoly Deal!")
	players = init_players.initialize_player_data()
	for i in players:
		print(draw_util.draw5(game_deck))
