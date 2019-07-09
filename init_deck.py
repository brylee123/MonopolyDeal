import random

class money_card():
	def __init__(self, value):
		self.value = value

class action_card(money_card):
	def __init__(self, value, name, description):
		super().__init__(value)
		self.name = name
		self.description = description

class property_card(money_card):
	def __init__(self, value, name, color, rent, buildable):
		super().__init__(value)
		self.name = name
		self.color = color
		self.rent = rent
		self.buildable = buildable

class property_wild(property_card):
	def __init__(self, value, property1, property2):
		super().__init__(value)
		self.property1 = property1
		self.property2 = property2

class rent_card(money_card):
	def __init__(self, value, color, wild):
		super().__init__(value)
		self.color = color # Set
		self.wild = wild # Boolean - Targeting

class property(Enum):
	RED = "red"
	DBLUE = "darkblue"
	LBLUE = "lightblue"
	PURPLE = "purple"
	GREEN = "green"
	ORANGE = "orange"
	YELLOW = "yellow"
	BROWN = "brown"
	RR = "railroad"
	UTIL = "utility"
	ALL = "all"

deck = {
	1: action_card(3, "House", "Add onto any full set you own to add $3M to rent value. (Except Railroads and Utilities)"), 
	2: action_card(3, "House", "Add onto any full set you own to add $3M to rent value. (Except Railroads and Utilities)"), 
	3: action_card(3, "House", "Add onto any full set you own to add $3M to rent value. (Except Railroads and Utilities)"), 
	4: action_card(4, "Hotel", "Add onto any full set you own to add $4M to rent value. (Except Railroads and Utilities)"), 
	5: action_card(4, "Hotel", "Add onto any full set you own to add $4M to rent value. (Except Railroads and Utilities)"), 
	6: action_card(4, "Hotel", "Add onto any full set you own to add $4M to rent value. (Except Railroads and Utilities)"), 
	7: action_card(2, "It's me birthday!", "All players give you $2M as a gift."), 
	8: action_card(2, "It's my birthday!", "All players give you $2M as a gift."),
	9: action_card(2, "It's my birthday!", "All players give you $2M as a gift."),
	10: action_card(1, "Double the Rent", "Needs to be played with a rent card."), 
	11: action_card(1, "Double the Rent", "Needs to be played with a rent card."), 
	12: action_card(5, "Deal Breaker", "Steal a complete set from any player (includes any buildings)"), 
	13: action_card(5, "Deal Breaker", "Steal a complete set from any player (includes any buildings)"), 
	14: action_card(4, "Just Say No!", "Use any time when an action card is played against you."), 
	15: action_card(4, "Just Say No!", "Use any time when an action card is played against you."), 
	16: action_card(4, "Just Say No!", "Use any time when an action card is played against you."), 
	17: action_card(3, "Debt Collector", "Force any player to pay you $5M"), 
	18: action_card(3, "Debt Collector", "Force any player to pay you $5M"), 
	19: action_card(3, "Debt Collector", "Force any player to pay you $5M"),
	20: action_card(3, "Sly Deal", "Steal a property from a player of your choice (cannot be a part of a full set)!"), 
	21: action_card(3, "Sly Deal", "Steal a property from a player of your choice (cannot be a part of a full set)!"), 
	22: action_card(3, "Sly Deal", "Steal a property from a player of your choice (cannot be a part of a full set)!"), 
	23: action_card(3, "Forced Deal", "Swap any propert with another player (cannot be part of a full set)!"), 
	24: action_card(3, "Forced Deal", "Swap any propert with another player (cannot be part of a full set)!"), 
	25: action_card(3, "Forced Deal", "Swap any propert with another player (cannot be part of a full set)!"), 
	26: action_card(3, "Forced Deal", "Swap any propert with another player (cannot be part of a full set)!"), 
	27: action_card(1, "Pass Go", "Draw two extra cards!"), 
	28: action_card(1, "Pass Go", "Draw two extra cards!"), 
	29: action_card(1, "Pass Go", "Draw two extra cards!"), 
	30: action_card(1, "Pass Go", "Draw two extra cards!"), 
	31: action_card(1, "Pass Go", "Draw two extra cards!"), 
	32: action_card(1, "Pass Go", "Draw two extra cards!"), 
	33: action_card(1, "Pass Go", "Draw two extra cards!"), 
	34: action_card(1, "Pass Go", "Draw two extra cards!"), 
	35: action_card(1, "Pass Go", "Draw two extra cards!"), 
	36: action_card(1, "Pass Go", "Draw two extra cards!"),
	37: property_card(2, "Electric Company", property.UTIL, [1, 2], True), 
	38: property_card(2, "Waterworks", property.UTIL, [1, 2], True), 
	39: property_card(2, "Pennsylvania Railroad", property.RR, [1,2,3, 4], True), 
	40: property_card(2, "Reading Railroad", property.RR, [1,2,3, 4], True), 
	41: property_card(2, "B. & O. Railroad", property.RR, [1,2,3, 4], True), 
	42: property_card(2, "Short Line Railroad", property.RR, [1,2,3, 4], True), 
	43: property_card(1, "Baltic Avenue", property.BROWN, [1, 2], True), 
	44: property_card(1, "Mediterranean Avenue", property.BROWN, [1, 2], True), 
	45: property_card(1, "Oriental Avenue", property.LBLUE, [1,2, 3], True),
	46: property_card(1, "Connecticut Avenue", property.LBLUE, [1,2, 3], True),
	47: property_card(1, "Vermont Avenue", property.LBLUE, [1,2, 3], True),
	48: property_card(2, "States Avenue", property.PURPLE, [1,2, 4], True),
	49: property_card(2, "Virginia Avenue", property.PURPLE, [1,2, 4], True),
	50: property_card(2, "St. Charles Place", property.PURPLE, [1,2, 4], True),
	51: property_card(2, "St. James Place", property.ORANGE, [1,3, 5], True),
	52: property_card(2, "Tennessee Avenue", property.ORANGE, [1,3, 5], True),
	53: property_card(2, "New York Avenue", property.ORANGE, [1,3, 5], True),
	54: property_card(3, "Indiana Avenue", property.RED, [2,3, 6], True),
	55: property_card(3, "Illinois Avenue", property.RED, [2,3, 6], True),
	56: property_card(3, "Kentucky Avenue", property.RED, [2,3, 6], True),
	57: property_card(3, "Atlantic Avenue", property.YELLOW, [2,4,6], True),
	58: property_card(3, "Marvin Gardens", property.YELLOW, [2,4,6], True),
	59: property_card(3, "Ventnor Avenue", property.YELLOW, [2,4,6], True),
	60: property_card(4, "Pennsylvania Avenue", property.GREEN, [2,4, 7], True),
	61: property_card(4, "Pacific Avenue", property.GREEN, [2,4, 7], True),
	62: property_card(4, "North Carolina Avenue", property.GREEN, [2,4, 7], True),
	63: property_card(4, "Park Place", property.DBLUE, [3, 8], True), 
	64: property_card(4, "Boardwalk", property.DBLUE, [3, 8], True), 
	65: property_wild(0, property.ALL, property.ALL), 
	66: property_wild(0, property.ALL, property.ALL), 
	67: property_wild(4, property.RR, property.LBLUE), 
	68: property_wild(2, property.RR, property.UTIL), 
	69: property_wild(4, property.RR, property.GREEN), 
	70: property_wild(4, property.GREEN, property.BLUE), 
	71: property_wild(3, property.YELLOW, property.RED), 
	72: property_wild(3, property.YELLOW, property.RED), 
	73: property_wild(1, property.LBLUE, property.BROWN), 
	74: property_wild(2, property.PURPLE, property.ORANGE), 
	75: property_wild(2, property.PURPLE, property.ORANGE), 
	76: rent_card(1, set(property.BROWN, property.LBLUE), False),
	77: rent_card(1, set(property.BROWN, property.LBLUE), False),
	78: rent_card(1, set(property.RED, property.YELLOW), False),
	79: rent_card(1, set(property.RED, property.YELLOW), False),
	80: rent_card(1, set(property.GREEN, property.DBLUE), False),
	81: rent_card(1, set(property.GREEN, property.DBLUE), False),
	82: rent_card(1, set(property.RR, property.UTIL), False),
	83: rent_card(1, set(property.RR, property.UTIL), False),
	84: rent_card(1, set(property.PURPLE, property.ORANGE), False),
	85: rent_card(1, set(property.PURPLE, property.ORANGE), False),
	86: rent_card(3, set(property.ALL), True), 
	87: rent_card(3, set(property.ALL), True), 
	88: rent_card(3, set(property.ALL), True), 
	89: money_card(1),
	90: money_card(1),
	91: money_card(1),
	92: money_card(1),
	93: money_card(1),
	94: money_card(1),
	95: money_card(2),
	96: money_card(2),
	97: money_card(2),
	98: money_card(2),
	99: money_card(2),
	100: money_card(3),
	101: money_card(3),
	102: money_card(3),
	103: money_card(4),
	104: money_card(4),
	105: money_card(4),
	106: money_card(5),
	107: money_card(5),
	108: money_card(10)
}

def shuffle_deck():
	game_deck = list(deck.keys())
	random.shuffle(game_deck)
	return game_deck
