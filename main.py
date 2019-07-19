import init_deck
import init_players
import draw_util
import pprint

def display_card(n):
	card = init_deck.get_card(n)
	card_details = 0
	print(type(card).__name__)
	print(vars(card))

	information = ""

	# Add print values of each card.

	if isinstance(card, init_deck.action_card):
		card.get_details()
		pass

	elif isinstance(card, init_deck.property_card):
		
		property_details1 = card.property1.color.value
		rent1 = ", ".join([str(i) for i in card.property1.rent]) 
		property_details1 = property_details1 + " (" + rent1 + ")"
		information = card.name + ": " + property_details1
		
		if card.property2 != None:
			property_details2 = card.property2.color.value
			rent2 = ", ".join([str(i) for i in card.property2.rent])
			property_details2 = property_details2 + " (" + rent2 + ")"

			information = card.name + ": " + property_details1 + " and " + property_details2
		print(information)

	elif isinstance(card, init_deck.rent_card):
		rentcolor1 = card.color.pop().value
		rentcolor2 = ""
		if len(card.color) > 0:
			rentcolor2 = card.color.pop().value
		print("Rent!: "+ rentcolor1 + " or " + rentcolor2)
	return card_details

if __name__ == '__main__':
	game_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	game_deck = init_deck.shuffle_deck()
	
	print("Welcome to Monopoly Deal!")
	players = init_players.initialize_player_data()
	for i in players:
		for j in draw_util.draw5(game_deck):
			display_card(j)
			print("\n")
			


		print("=========================================")
			
