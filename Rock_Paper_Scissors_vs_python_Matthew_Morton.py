import random

name = input("Enter your name: ")
python_score = 0
user_score = 0
game_on = True
print(f"Welcome, {name.title()}! Let's get ready to play Rock, Paper, Scissors!")

while True:
	user_action = input("Enter a choice: (rock, paper, or scissors): ")

	possible_actions = ["rock", "paper", "scissors"]
	python_action = random.choice(possible_actions)

	print(f"\nYou chose {user_action}, Python chose {python_action}.\n")

	if user_action == python_action:
		print(f"Both players drew {user_action}. It's a tie! Shoot again!")

	elif user_action == "rock":
		if python_action == "scissors":
			print("Rock crushes scissors! You win!")
			user_score += 1
		else:
			print("Paper covers rock. You lose!")
			python_score += 1

	elif user_action == "paper":
		if python_action == "rock":
			print("Paper covers rock! You win!")
			user_score += 1
		else:
			print("Scissors cuts paper! You lose!")
			python_score += 1

	elif user_action == "scissors":
		if python_action == "paper":
			print("Scissors cuts paper! You win!")
			user_score += 1
		else:
			print("Rock smashes scissors! You lose!")
			python_score += 1



	print("\n\t-----Score Board-----")
	print(f"\tYou: {user_score} <- | -> Python: {python_score}")	

	play_again = input("\nPlay again? (yes/no): ")
	if play_again.lower() != "yes":
		break
	
if user_score > python_score:
	print(f"\t\nYou won, {name.title()}!! Let's play again sometime!")
elif user_score == python_score:
	print("It's a tie! Don't quit now... Settle the Score!")
	play_again = input("\nPlay again? (yes/no): ")
	if play_again.lower() != "yes":
		print("\t\nFine, quitter! It's a draw!")
else:
	print(f"\t\nYou lost, {name.title()}! Better luck next time!")


