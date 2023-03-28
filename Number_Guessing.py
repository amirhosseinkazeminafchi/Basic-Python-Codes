import random
userWon=0 #when this variable's value is 0, it means the player hasn't yet guessed the right number.
def game(number):
	global userWon
	try:

		guess= int(input("Enter your guess: "))
		if guess>100 or guess<0:
			raise Exception

	except Exception as e:

		print("Either number out of range, or non-numeric value entered.")
		print(e)

	else:

		if guess==number:

			print("Your guess is right.")
			userWon=1 #value of this variable turns to 1 when the player guesses the number correctly and the programends.

		else: #if the user doesn't guess correctly for the first time, the player is told how close he is to the correct answer.
			difference= guess - number
			if difference<0:
				if (difference> -10): 
					print ("Your guess is less than the actual number. ")
				else:
					print("Your guess is far less than the actual number. ") #the assumption here is that if the guess is more than 10 less than the actual number, the guess is FAR LESS than the actual number.

			else:
				if (difference<=10):
					print("Your guess is greater than the actual number.")
				else:
					print("Your guess if far greater than the actual number.") #the assumption here is that if the guess is more than 10 more than the actual number, the guess is FAR GREATER than the actual number.
			return userWon 

def main():
	number= random.randint(1, 101)
	print("The number is between 1 and 100, inclusively.") #Gives instruction to the user to not enter any number greater than 100, and less than 0.
	game(number)
	if userWon!=1:
		print("Guesses left=4.")
		game(number)
		if userWon!=1:
			print("Guesses left=3.")
			game(number)
			if userWon!=1:
				print("Guesses left=2.")
				game(number)
				if userWon!=1:
					print("Guesses left=1.")
					game(number)
					if userWon!=1:
						print("You have lost. The correct number is ",number)

main()