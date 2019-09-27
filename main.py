import init_deck
import init_players
import card_util
#import pprint

if __name__ == '__main__':
	game_deck = init_deck.shuffle_deck()
	
	print("Welcome to Monopoly Deal!")
	players = init_players.initialize_player_data()
	for player in players:
		print(player.name)
		player.hand = card_util.draw5(game_deck)

		for card in player.hand:
			card_util.display_card(card)
		print("=========================================")
			
	# Player hands shound be initialized at this point

	while True:
		for player in players:
			player.hand.extend(card_util.draw2(game_deck))
			print(player.hand)
		break