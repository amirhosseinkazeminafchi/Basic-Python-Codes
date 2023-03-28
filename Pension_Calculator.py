#calculates employees age from his date of birth and current date
def ageCalculator(birthDate, currentDate): 

	age= int(currentDate[4:]) - int(birthDate[4:])
	month= int(currentDate[2:4])- int(birthDate[2:4])
	if month<0: #if the month in the current date is less than the month in employee's birthday, it means his birthday is yet to come, so 1 is subtracted from the difference of years of current date and birthday. 
		age=age-1
	return age

def errorChecker(currentDate, joinDate, birthDate, marriageDate):
#{0:2} extracts the DATE; whereas [2:4] extracts the month to check they don't exceed 12 and 31, respectively.
	var01=int(currentDate[2:4])
	var02=int(currentDate[0:2])
	var03=int(joinDate[2:4])
	var04=int(joinDate[0:2])
	var05=int(birthDate[2:4])
	var06=int(birthDate[0:2])

	if len(marriageDate)==8: #marriageDate will only be checked for errors if a valid marriageDate was entered(i.e an eight digit date), otherwise it will be considered that the employee isn't married.

		var07=int(marriageDate[2:4])
		var08=int(marriageDate[0:2])

	else:
		var07, var08= 0,0

	if len(currentDate)!=8 or len(joinDate)!=8 or len(birthDate)!=8:
		print("One or all of the dates entered is/are invalid. Program is restarting.")
		main()

	elif var01>12 or var03>12 or var05>12 or var07>12 or var02>31 or var04>31 or var06>31 or var08>31:
		print("You either entered incorrect day or incorrect month in one of the dates. Program is restarting.")
		main()

def basicSalaryfunc(basicSalary):

	incomeTax= 0.05*basicSalary
	provincialTax= 0.07*basicSalary
	print("Your Income Tax is: ", incomeTax)
	print("Your Provincial Tax is: ",provincialTax)
	basicSalary= basicSalary-incomeTax-provincialTax
	print("Your basic salary after tax deductions is :", basicSalary)
	return basicSalary


def houseRentfunc(basicSalary, marriageDate):

	if len(marriageDate)==8: #If length of the marriageDate is 8, it means the employee is married. (He entered a valid date.)
		
		houseRent= 0.15*basicSalary

	else:

		houseRent=0 #If length of the date isn't 8, it means he's not married, so should get 0 house rent.
	print("Your house rent is: ", houseRent)
	return houseRent

def allowancefunc(age,basicSalary): #makes use of formulas to calculate the value of allowance an employee is supposed to get.

	if age>=45 and age<=55: 
		allowance= 0.10*basicSalary
	elif age>55:
		allowance= 0.15*basicSalary
	else:
		allowance=0
	print("Your old age allowance is: ",allowance)
	return allowance

def monthsInServicefunc(currentDate, joinDate):

	year= int(currentDate[4:])-int(joinDate[4: ])
	months= int(currentDate[2:4])-int(joinDate[2:4])
	monthsInService= (year*12) + months
	if year<0 or monthsInService<0: #if either of these conditions is true, it would mean the current date user entered is lesser than the joining date, which isn't logically possible.
		print("You entered an invalid current date or join date in the program. Exiting...")
		exit()
	return monthsInService

def monthsSinceMarriagefunc(currentDate, marriageDate):

	year= int(currentDate[4:])-int(marriageDate[4: ])
	months= int(currentDate[2:4])-int(marriageDate[2:4])
	monthsSinceMarriage= (year*12) + months #calculates the months user has served since marriage, if the result of "months" variable is negative, that number would simply be subtracted from the months inservice. 
	return monthsSinceMarriage

def totalSalaryfunc(basicSalary, houseRent, allowance):

	totalSalary= basicSalary + houseRent + allowance
	print("Your total salary i.e. Basic Salary + House Rent + Allowance is : ",totalSalary)
	return totalSalary

def pensionCalcfunc(marriageDate,currentDate, joinDate, basicPay, houseRent, totalSalary, allowance):

	monthsInService=monthsInServicefunc(currentDate, joinDate)

	if len(marriageDate)==8 :
		
		monthsSinceMarriage= monthsSinceMarriagefunc(currentDate, marriageDate) #calls the months in service since marriage function if the employee is married or declares its value to be 0 if the employee isn't married.
	
	else:
		
		monthsSinceMarriage= 0
	
	pension= ((basicPay*2)*monthsInService) + (houseRent*monthsSinceMarriage) + (allowance*3) + (totalSalary*2)
	print("                          *** Pension Calculation ***                                       ")
	print("The pension is calculated according to the following formula:")
	print("Basic salary is doubled and multiplied with months in service:     ", basicPay*2*monthsInService)
	print("Rent of house is multiplied by months in service since marriage:  +", houseRent*monthsSinceMarriage)
	print("Old age allowance is tripled:                                     +", allowance*3)
	print("Total salary is doubled:                                          +", totalSalary*2)
	print("Toal pension                                                      =", pension)

def main():

	try:
		
		basicSalary= int(input("Enter your basic pay: "))
		basicPay=basicSalary #The variable basicSalary's value will change as it is used in functions to calculate home rent and allowances, so it's initial value is stored in another variable to be used later for calculating pension.
		
		if basicSalary<0:
			raise Exception
		currentDate= input("Input current date in DDMMYYYY format: ")
		
		if len(currentDate)>8 or len(currentDate)<8:
			raise Exception
		joinDate= input("Input the date the joined in DDMMYYYY format:")
		
		if len(joinDate)>8 or len(joinDate)<8:
			raise Exception
		birthDate= input("Enter your date of birth in DDMMYYYY format: ")
		age= ageCalculator(birthDate, currentDate) #returns the age of the person and makes sure it's not illogical.
		
		if age<0 or age>100: 
			raise Exception
		marriageDate=input("Enter your marriage date in DDMMYYYY format or enter nothing if you're not married:") #If the user is married, he has to type an 8 digit date, if he types ANYTHING else, the program will assume that he's not married. 
				
	except Exception as e:

		print("Invalid Input. ")
		print(e)

	else:

		errorChecker(currentDate, joinDate, birthDate, marriageDate) #It will check if for any of the input dates whether the month entered exceeds 12 or the day entered exceeds 31.
		basicSalary= basicSalaryfunc(basicSalary) #deducts the taxes from the basicSalary to be used to calculate houseRent and allowance
		houseRent= houseRentfunc(basicSalary, marriageDate) #calulates the value of houseRent for married employees
		allowance= allowancefunc(age,basicSalary) #calculates the value of allowance for all employees aged 45 or more.
		totalSalary= totalSalaryfunc(basicSalary, houseRent, allowance) #adds up all three components of the salary
		pension= pensionCalcfunc(marriageDate,currentDate, joinDate, basicPay,houseRent, totalSalary, allowance) #computes the pension of the employee using the provided formula
		#add a suitable printing method over here
main()