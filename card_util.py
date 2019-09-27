import init_deck

def draw2(game_deck):
	# Use for start of each turn and pass go
	card1 = game_deck.pop()
	card2 = game_deck.pop()

	return [card1, card2]

def draw5(game_deck):
	# Use for dealing in the beginning and if player has no cards
	card1 = game_deck.pop()
	card2 = game_deck.pop()
	card3 = game_deck.pop()
	card4 = game_deck.pop()
	card5 = game_deck.pop()

	return [card1, card2, card3, card4, card5]

def display_card(n):
	card = init_deck.get_card(n)
	card_details = 0
	#print(type(card).__name__) # Class Name
	#print(vars(card)) # Object Attributes/Member Variables
	#print(n)
	information = ""	# Add print values of each card.

	# If action_card
	if isinstance(card, init_deck.action_card):
		information = "[$"+str(card.value)+"] " + card.name + ": " + card.description

	# If property_card
	elif isinstance(card, init_deck.property_card):

		property_details1 = card.property1.color.value

		# Property wild card - 10 colors
		if n == 65 or n == 66:
			print("Wild Card. This card can be used as part of any property set. This card has no monetary value.")
			return

		rent1 = ", ".join([str(i) for i in card.property1.rent]) 
		property_details1 = property_details1 + " (" + rent1 + ")"
		information = "[$"+str(card.value)+"] " + card.name + ": " + property_details1
		
		if card.property2 != None:
			property_details2 = card.property2.color.value
			rent2 = ", ".join([str(i) for i in card.property2.rent])
			property_details2 = property_details2 + " (" + rent2 + ")"

			information = "[$"+str(card.value)+"] " + card.name + ": " + property_details1 + " and " + property_details2

	# If rent_card
	elif isinstance(card, init_deck.rent_card):
		rentcolor1 = card.color.pop().value
		rentcolor2 = ""
		if len(card.color) > 0:
			rentcolor2 = card.color.pop().value
		information = "[$"+str(card.value)+"] " + "Rent!: "+ rentcolor1

		if len(rentcolor2) > 0:
			information += " or " + rentcolor2

	# If money_card
	elif isinstance(card, init_deck.money_card):
		information = "[$"+str(card.value)+"] Money"

	print(information)
	return