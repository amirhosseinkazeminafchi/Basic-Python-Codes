def upper(string): #converts all letters in the string to uppercase

	global upperCase, lowerCase

	for a in range(len(string)):

		for b in range(len(lowerCase)):

			if string[a]==lowerCase[b]:
				string= replaceAll(string, string[a], upperCase[b])

	return string

def lower(string): #converts all letters in the string to lowerCase

	global upperCase, lowerCase

	for a in range(len(string)):

		for b in range(len(upperCase)):

			if string[a]==upperCase[b]:
				string= replaceAll(string, string[a], lowerCase[b])

	return string

def endsWith(string, find): 		#Return "True" if the string Endswith the parameter "find", else returns False.1

	for i in range(len(string)):

		if find==string[len(string) - len(find): ]:
			
			flag=True

		else:

			flag=False

	return flag

def startsWith(string, find): #Returns "True" if the string StartsWith the parameter "Find", else returns False.2
	for i in range(len(string)):

		if find==string[ : len(find)]:

			flag=True

		else:

			flag=False

	return flag

def repetition(string, find): #Returns the number of times a given parameter exists/comes in the string. 3

	reps= 0

	for i in range(len(string)):

		if find == string[ i : i + len(find)]:

			reps+=1

	return reps

def isFound(string, find): #Tells if a given parameter "Find" exists in the string or not. Returns either True or False.4

	flag=False

	for i in range(len(string)):

		if find== string[ i : i + len(find)]:

			flag=True
			break

	return flag

def replaceAll(string, toBeReplaced, replaceWith): #replaces all instances where the parameter "to be replaced" occurs in the string with the parameter "replace with."5

	for i in range(len(string)):

		if toBeReplaced== string[ i : i + len(toBeReplaced)]:

			string= string[ 0: i ] + replaceWith + string[ i + len(toBeReplaced) : ]

	return string

def replaceSome(string, toBeReplaced, replaceWith, iterations): #replaces a certain number of instances (provided by the user through "iterations" parameter) where the parameter "to be replaced" occurs in the string with the parameter "replace with."6

	count=0

	for i in range(len(string)):

		if toBeReplaced == string[i : i +len(toBeReplaced)]:

			string= string[ 0 : i ] + replaceWith + string[ i + len(toBeReplaced) : ]
			count+=1

		if count==iterations:

			break

	return string 

def index(string, find): #returns the index of the first letter of the item/string/word you wish to find in a string.  7

	index= -1

	for i in range(len(string)):

		if find== string[ i : i + len(find)]:

			index= i
			break

	return index

def indexFrom(string, find, startIndex):	#returns the index of the first letter of the word you search for in a string; it starts the search from the index that you pass on as a paramter "startIndex". 8

	index = -1

	while(startIndex < len(string)):
		
		if find==(string[startIndex:startIndex +len(find)]):

			index = startIndex
			break

		else:

			startIndex += 1

	return index

def rightFind(string, find): #returns the index of the first character of the string to be found, and starts it search from the end of the string and moves to the left. 9

	index=-1

	for i in range(len(string), -1, -1):

		if find == string [i - len(find) : i]:

			index= i - len(find)
			break

	return index 

def middleFind(string, find): #starts its search from the middle of the string, and returns the index of the first character of the string being searched in a given string.

	index=-1

	for i in range(len(string)//2, len(string)):

		if(string[i:i+(len(find))] == find):

			index= i
			break

	return index

def swapCase(string): #Turns uppercase to lowercase and lowercase to upperCase.

	global lowerCase, upperCase
	counter=0 

	for var in string:

		for i in range(len(lowerCase)):

			if var == upperCase[i]:
               
				string = replaceAll(string,string[counter],lowerCase[i])

			elif var == lowerCase[i]:

				string = replaceAll(string,string[counter],upperCase[i])

		counter +=1

	return string

def isUpper(string): #tells whether the whole string is in uppercase or Not.

	count=0

	for i in range(len(string)):

		for j in range(len(upperCase)):

			if string[i]==upperCase[j]:
				count+=1
				break

	if count==len(string):
		return True

	else:
		return False

def isLower(string): #tells whether the whole string is in lowercase or Not.

	count=0

	for i in range(len(string)):

		for j in range(len(upperCase)):

			if string[i]==lowerCase[j]:
				count+=1
				break

	if count==len(string):
		return True

	else:
		return False

def capitalize(string): #Turns the first letter of the string to uppercase if it's not already. 

	for i in range(len(lowerCase)):
		
		if string[0]==lowerCase[i]:
			string= upperCase[i]+string[1:]

	return string

def reverse(string): #reverses a string

	list01=[]
	str01=""

	for a in range(len(string)):

		list01.append(string[a])

	for b in range(1, len(list01)+1):

		str01+=list01[len(list01)-b]

	return str01

def isAlpha(string):				#returns true if all the characters in the string are alphabets or dots, else returns False.
	
	global lowerCase, upperCase

	for i in range(len(string)):
		
		flag=False

		for b in range(len(lowerCase)):

			if string[i]== lowerCase[b] or string[i]==upperCase[b]:

				flag=True

		if not(flag):

			break

	return flag

upperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digits = ["0",'1','2','3','4','5','6','7','8','9']