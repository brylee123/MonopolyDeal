from enum import Enum

class input_conditions(Enum):
	PLAYER_COUNT = 1

def validate_input(input_txt, condition, err_msg):
	user_input = input(input_txt)

	while True:
		if condition == input_conditions.PLAYER_COUNT:
			if not user_input.isdigit() or (int(user_input) < 2 or int(user_input) > 5):
				print(err_msg)
				user_input = input(input_txt)
			else:
				break
		else:
			break

	return user_input


player_count = validate_input("Enter player count: ", input_conditions.PLAYER_COUNT, "Please enter a valid number between 2 and 5")
