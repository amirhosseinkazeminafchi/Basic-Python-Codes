import random

def initialChecker(dealerCard01, dealerCard02, playerCard02, playerCard01):

	print("You get an %d and a %d." %(playerCard01, playerCard02)) #Shows the cards of the player

	dealerSum= dealerCard01 + dealerCard02
	playerSum= playerCard01 + playerCard02

	print("Your total is %d. \nThe dealer has a %d showing, and a hidden card. \nHis total is hidden, too." %(playerSum, dealerCard01))

	flag= checker(dealerSum, playerSum) #checks if the dealer or the player have won with their intial cards.

	if flag==False:
		nextRound(dealerSum, playerSum, dealerCard02) #if neither have won with the intitial cards, it allows the player to hit for as many times as he wants.

def checker(playerSum, dealerSum):

	flag=False

	if dealerSum==21 and playerSum!= 21:
		print("The Dealer wins!")
		flag= True

	elif playerSum==21 and dealerSum!=21:
		print("You win!")
		flag= True

	elif playerSum>21 and dealerSum<21:
		print("You have busted. Dealer wins!")
		flag= True

	elif dealerSum>21 and playerSum<21:
		print("The dealer has busted. You win!")
		flag = True

	elif dealerSum>21 and playerSum>21:
		print("The dealer wins.")
		flag=True

	return flag

def nextRound(dealerSum, playerSum, dealerCard02):

	for i in range(10): 

		response01= input("Would you like to hit or stay? ")

		if response01=="hit":

			playerNew= random.randint(2,11)
			playerSum+=playerNew

			print("You draw a %d.\nYour total is %d." %(playerNew, playerSum))
			flag= checker(playerSum, dealerSum) #each time the player hits, this function is called to make sure that the player hasn't busted and lost already.

			if flag==True:
				break

		elif response01=="stay":

			print ("Okay. Dealer's turn.\nHis hidden card was a %d. \nHis total was %d "%(dealerCard02, dealerSum)) #shows the player the hidden card of the dealer when he decides to stay.
			
			for a in range(10):

				if dealerSum<=16: #dealer continues to hit till his sum of cards is less than 17.

					dealerNew= random.randint(2,11)
					dealerSum+=dealerNew

					print("Dealer chooses to hit. \nHe draws an %d. \nHis total is %d."%(dealerNew, dealerSum))
					flag= checker(playerSum, dealerSum) #checks each time the dealer hits, if he has busted and lost.

				elif dealerSum>16:

					print("Dealer stays. ")
					
					if dealerSum==playerSum:
					
						print("Dealer wins.") #Incase of a tie, the dealer wins.
						flag=True
					
					else:

						if dealerSum>playerSum:
							print("Dealer wins.") #Compares the totals of both players, which one has the higher wins. 
							flag=True

						else:
							print("Player wins.")
							flag=True

				if flag==True: #Flag has been assigned a truth value in the code above wherever the game's result has been decided.
					break

		if flag==True: #Flag has been assigned a truth value in the code above wherever the game's result has been decided.
			break

def main():

	dealerCard01= random.randint(2,11)
	dealerCard02= random.randint(2,11)
	playerCard01= random.randint(2,11)
	playerCard02= random.randint(2,11)

	initialChecker(dealerCard01, dealerCard02, playerCard02, playerCard01)

main()