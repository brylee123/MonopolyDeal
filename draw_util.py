def draw2(game_deck):
	# Use for start of each turn and pass go
	card1 = game_deck.pop()
	card2 = game_deck.pop()

	return card1, card2

def draw5(game_deck):
	# Use for dealing in the beginning and if player has no cards
	card1 = game_deck.pop()
	card2 = game_deck.pop()
	card3 = game_deck.pop()
	card4 = game_deck.pop()
	card5 = game_deck.pop()

	return card1, card2, card3, card4, card5

