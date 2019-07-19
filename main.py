import init_deck
import init_players
import draw_util
import pprint

def display_card(n):
	card_details = 0
	return card_details

if __name__ == '__main__':
	game_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	game_deck = init_deck.shuffle_deck()
	
	
	print("Welcome to Monopoly Deal!")
	players = init_players.initialize_player_data()
	for i in players:
		for j in draw_util.draw5(game_deck):
			card = init_deck.get_card(j)
			
			print(type(card).__name__)

			print(vars(card))
			if isinstance(card, init_deck.action_card):
				#card.get_details()
				pass
		print("=========================================")
			
