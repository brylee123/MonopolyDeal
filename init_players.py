from enum import Enum

class input_conditions(Enum):
	PLAYER_COUNT = 1
	USER_NAME = 2

class player():
	def __init__(self, number, name, hand, property_field, money_field):
		self.number = number
		self.name = name
		self.hand = hand
		self.property_field = property_field
		self.money_field = money_field

def validate_input(input_txt, condition, err_msg):
	user_input = input(input_txt)

	while True:
		if condition == input_conditions.PLAYER_COUNT:
			if not user_input.isdigit() or (int(user_input) < 2 or int(user_input) > 5):
				print(err_msg)
				user_input = input(input_txt)
			else:
				break

		if condition == input_conditions.USER_NAME:
			if not user_input.isalnum() or len(user_input) > 10 or len(user_input) < 1:
				print(err_msg)
				user_input = input(input_txt)
			else:
				break
		else:
			break

	return user_input

def initialize_player_data():
	'''
	players = []
	player_count = validate_input("Enter player count: ", input_conditions.PLAYER_COUNT, "Please enter a valid number between 2 and 5")
	player_count = int(player_count)

	for i in range(1, player_count+1):
		player_name = validate_input("Enter player "+str(i)+"'s name: ", input_conditions.USER_NAME, "Please enter an alphanumeric string less than 10 characters")
		
		while player_name in players:
			print("Players cannot have the same name as existing players. Think harder and be unique.")
			player_name = validate_input("Enter player "+str(i)+"'s name: ", input_conditions.USER_NAME, "Please enter an alphanumeric string less than 10 characters")
		
		players.append(player(i, player_name, [], [], []))

	
	'''
	########################################
	player_count = 5
	players = [	player(1, "alice", [], [], []),
				player(2, "bob", [], [], []), 
				player(3, "carrie", [], [], []), 
				player(4, "doris", [], [], []),
				player(5, "edith", [], [], [])]
	#DELETE
	########################################
	

	print("\n\nAll set! Here are the players!")
	for i in range(player_count):
		print("Player "+ str(i+1) +": ", players[i].name)

	return players