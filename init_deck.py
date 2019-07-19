import random
from enum import Enum

class money_card():
	def __init__(self, value):
		self.value = value

class action_card(money_card):
	def __init__(self, value, name, description):
		super().__init__(value)
		self.name = name
		self.description = description

class property_type():
	def __init__(self, color, rent, buildable):
		self.color = color
		self.rent = rent
		self.buildable = buildable

class property_card(money_card):
	def __init__(self, value, name, property1, property2=None):
		super().__init__(value)
		self.property1 = property1
		self.property2 = property2
		self.name = name
		self.wild = False
		if not property2 == None:
			self.wild = True

class rent_card(money_card):
	def __init__(self, value, color, wild):
		super().__init__(value)
		self.color = color # Set
		self.wild = wild # Boolean - Targeting

class property(Enum):
	RED = "Red"
	BLUE = "Dark Blue"
	LBLUE = "Light Blue"
	PURPLE = "Purple"
	GREEN = "Green"
	ORANGE = "Orange"
	YELLOW = "Yellow"
	BROWN = "Brown"
	RR = "Railroad"
	UTIL = "Utility"
	ALL = "All"

util = property_type(property.UTIL, [1, 2], False)
railroad = property_type(property.RR, [1, 2, 3, 4], False)
brown = property_type(property.BROWN, [1, 2], True)
light_blue = property_type(property.LBLUE, [1, 2, 3], True)
purple = property_type(property.PURPLE, [1, 2, 4], True)
orange = property_type(property.ORANGE, [1, 3, 5], True)
red = property_type(property.RED, [1, 2, 4], True)
yellow = property_type(property.YELLOW, [2, 4, 6], True)
green = property_type(property.GREEN, [2, 4, 7], True)
blue = property_type(property.BLUE, [3, 8], True)
wild = property_type(property.ALL, None, None)

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
	37: property_card(2, "Electric Company", util, None), 
	38: property_card(2, "Waterworks", util, None), 
	39: property_card(2, "Pennsylvania Railroad", railroad, None), 
	40: property_card(2, "R eading Railroad", railroad, None), 
	41: property_card(2, "B. & O. Railroad", railroad, None), 
	42: property_card(2, "Short Line Railroad", railroad, None), 
	43: property_card(1, "Baltic Avenue", brown, None), 
	44: property_card(1, "Mediterranean Avenue", brown, None), 
	45: property_card(1, "Oriental Avenue", light_blue, None),
	46: property_card(1, "Connecticut Avenue", light_blue, None),
	47: property_card(1, "Vermont Avenue", light_blue, None),
	48: property_card(2, "States Avenue", purple, None),
	49: property_card(2, "Virginia Avenue", purple, None),
	50: property_card(2, "St. Charles Place", purple, None),
	51: property_card(2, "St. James Place", orange, None),
	52: property_card(2, "Tennessee Avenue", orange, None),
	53: property_card(2, "New York Avenue", orange, None),
	54: property_card(3, "Indiana Avenue", red, None),
	55: property_card(3, "Illinois Avenue", red, None),
	56: property_card(3, "Kentucky Avenue", red, None),
	57: property_card(3, "Atlantic Avenue", yellow, None),
	58: property_card(3, "Marvin Gardens", yellow, None),
	59: property_card(3, "Ventnor Avenue", yellow, None),
	60: property_card(4, "Pennsylvania Avenue", green, None),
	61: property_card(4, "Pacific Avenue", green, None),
	62: property_card(4, "North Carolina Avenue", green, None),
	63: property_card(4, "Park Place", blue, None), 
	64: property_card(4, "Boardwalk", blue, None),
	65: property_card(0, "Wild Card", wild, wild), 
	66: property_card(0, "Wild Card", wild, wild), 
	67: property_card(4, "Wild Card", railroad, blue),
	68: property_card(2, "Wild Card", railroad, util), 
	69: property_card(4, "Wild Card", railroad, green), 
	70: property_card(4, "Wild Card", green, blue), 
	71: property_card(3, "Wild Card", yellow, red), 
	72: property_card(3, "Wild Card", yellow, red), 
	73: property_card(1, "Wild Card", light_blue, brown), 
	74: property_card(2, "Wild Card", purple, orange), 
	75: property_card(2, "Wild Card", purple, orange), 
	76: rent_card(1, {property.BROWN, property.LBLUE}, False),
	77: rent_card(1, {property.BROWN, property.LBLUE}, False),
	78: rent_card(1, {property.RED, property.YELLOW}, False),
	79: rent_card(1, {property.RED, property.YELLOW}, False),
	80: rent_card(1, {property.GREEN, property.BLUE}, False),
	81: rent_card(1, {property.GREEN, property.BLUE}, False),
	82: rent_card(1, {property.RR, property.UTIL}, False),
	83: rent_card(1, {property.RR, property.UTIL}, False),
	84: rent_card(1, {property.PURPLE, property.ORANGE}, False),
	85: rent_card(1, {property.PURPLE, property.ORANGE}, False),
	86: rent_card(3, {property.ALL}, True), 
	87: rent_card(3, {property.ALL}, True), 
	88: rent_card(3, {property.ALL}, True), 
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

def get_card(n):
	return deck[n]

def shuffle_deck():
	game_deck = list(deck.keys())
	random.shuffle(game_deck)
	return game_deck
