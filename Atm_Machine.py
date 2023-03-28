def atmMachine (pins,accountNumbers,userNames,accountBalance):
	
	for x in range(1,100000000000000000):
	
		count=0 
	
		try:
			
			pinCode = int(input("Enter your 4 digit pin: "))
			
		except Exception as e:
	
			print("Invalid pin entered.")
			print(e)
	
		else:

			found=False

			for pin in pins:
	
				if pin==pinCode:

					found=True
					print("Welcome :",userNames[count])
					print("Your account number is :", accountNumbers[count])
					print("Your current account balance is: ", accountBalance[count])
					accBalance= int(accountBalance[count])
					transType = input("Please select a transaction type: d for deposit/ w for withdrawal: ")
		
					if transType == "d":

						try:
		
							depAmount = int(input("Enter the amount you want to deposit: "))
							
						except Exception as e:
						
							print("Invalid input of deposit amount. Please try again")
							print(e)

						else:
						
							accBalance+=depAmount 
							accountBalance[count]= accBalance #the deposited amount is added to the current balance and stored in the list. 
							print("Your new balance is: ",accBalance, ".Have a nice day!")

					else:
						
						try:
					
							withdrawalAmount = int(input("Enter the amount you want to withdraw: "))
					
						except Exception as e:
					
							print("Invalid input of withdrawal amount. Please try again.")
							print(e)

						else:
								
							accBalance-=withdrawalAmount

							if accBalance<0: 
								
								print("You do not have sufficient funds in your account. ") #prints an error message if the user tries to withdraw more money than he has in his account.
								accBalance+=withdrawalAmount
								continue

							accountBalance[count]= accBalance #the amount withdrawn is subtracted from current balance, and the new balance is stored in the list.
							print("Your new balance is:",accBalance,".Have a nice day!")
			
				count+=1 #value of count is incremented for the inner loop, so that if the pin is not found in the first index, the next index is searched,  till the end index is reached.
			if found==False:

				print("Your pin code doesn't match any account number in the system. Please try again. ")

def main():
	
	pins = [1122, 1234, 1000, 2000, 3000] #lists containing pins, accountNo.s etc in sequence, the first pin in PINS is for the First user name is userNames list.
	accountNumbers = [123456789, 987654321, 125896347, 123456781, 321456987]
	userNames = ["Junaid Khalid","Muhammad Khalid","Husnain Khalid","Talha Khalid","Waleed Khalid"]
	accountBalance = [50000000,1000000,350000,250000,2540000]
	atmMachine (pins,accountNumbers,userNames,accountBalance)

main()