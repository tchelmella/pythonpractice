import random

a = False

while(not a):
	choice1 = input("Enter your choice Rock, Paper or Scissors")
	choice2 = input("Enter your choice Rock, Paper or Scissors")

	if(choice1 == choice2):
		print("Game Draw")
	elif(choice1 == 'Rock' and choice2 == 'Paper'):
		print("Player2 Wins")
	elif(choice1 == 'Rock' and choice2 == 'Scissors'):
		print("Player1 Wins")
	elif(choice1 == 'Paper' and choice2 == 'Rock'):
		print("Player1 Wins")
	elif(choice1 == 'Paper' and choice2 == 'Scissors'):
		print("Player2 Wins")
	elif(choice1 == 'Scissors' and choice2 == 'Rock'):
		print("Player2 Wins")
	elif(choice1 == 'Scissors' and choice2 == 'Paper'):
		print("Player1 Wins")
	else:
		print('Wrong input, Please enter either Rock, Paper or Scissors')


	play = input("Do you want to start a new game? Yes or No")

	if play == 'Yes' or 'yes' or 'y':
		print("New game will start")
	elif play == 'No' or 'no' or 'n':
		a = True
		print("Game Over")
	else:
		print("Wrong input, please type Yes or No")


