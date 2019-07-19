from enum import Enum

class input_conditions(Enum):
	PLAYER_COUNT = 1
	USER_NAME = 2

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


player_count = validate_input("Enter player count: ", input_conditions.PLAYER_COUNT, "Please enter a valid number between 2 and 5")
player_count = int(player_count)

players = []
for i in range(1, player_count+1):
	player_name = validate_input("Enter player "+str(i)+"'s name: ", input_conditions.USER_NAME, "Please enter an alphanumeric string less than 10 characters")
	
	while player_name in players:
		print("Players cannot have the same name as existing players. Think harder and be unique.")
		player_name = validate_input("Enter player "+str(i)+"'s name: ", input_conditions.USER_NAME, "Please enter an alphanumeric string less than 10 characters")
	players.append(player_name)

print("\n\nAll set! Here are the players!")
for i in range(1, player_count+1):
	print("Player "+ str(i) +": "+players[i-1])
