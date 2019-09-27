import init_deck
import init_players
import card_util
import pprint

if __name__ == '__main__':
	#game_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	game_deck = init_deck.shuffle_deck()
	
	print("Welcome to Monopoly Deal!")
	players = init_players.initialize_player_data()
	for i in players:
		for j in card_util.draw5(game_deck):
			card_util.display_card(j)
			print("\n")
			
		print("=========================================")
			