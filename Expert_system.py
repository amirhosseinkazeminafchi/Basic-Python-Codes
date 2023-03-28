print(''' Below is a list of symptoms that this system can handle: 
1.Headache
2.Aggression
3.Night sweats
4.Nocturnal coughs
5.Itchy scalp
6.Back pain
7.Blurred vision
8.Nausea
9.Dizziness
10.Blisters & Skin rashes
11.Red Eyes
12.Joint pain''')

def medication(disease): #takes the name of the disease as an input, and suggests a medicine for it. 

	if disease=="altitude sickness":
		print("Suggested Medicine: Acetazolamide")

	if disease=="hypertension":
		print("Suggested Medicine: Propranolol")

	if disease=="HIV":
		print("Suggested Medicine: Antiretroviral drug")

	if disease=="headache":
		print("Suggested Medicine: Disprin")		

	if disease=="alzheimer":
		print("Suggested Medicine: Haloperidol")

	if disease=="arthritis":
		print("Suggested Medicine: Meclofenamic acid")

	if disease=="myocardial infarction":
		print("Suggested Medicine: Streptokinase")

	if disease=="asthma":
		print("Suggested Medicine: Zileuton")

	if disease=="alopecia":
		print("Suggested Medicine: Minoxidil")

	if disease=="bladdercancer":
		print("Suggested Medicine: Radiation therapy")

	if disease=="braintumor":
		print("Suggested Medicine: Radiation therapy")

	if disease=="dehydration":
		print("Suggested Medicine: Water")

	if disease=="hepatitis":
		print("Suggested Medicine: Telbivudine")

	if disease=="cardiovascular":
		print("Suggested Medicine: ACE inhibitor")

	if disease=="heartfailure":
		print("Suggested Medicine: Cyclothiazide")

	if disease=="dermatitis":
		print("Suggested Medicine: Ketoconazole")

	if disease=="influenza":
		print("Suggested Medicine: Amantadine")

	if disease=="leukemia":
		print("Suggested Medicine: Irinotecan")

def simpleMed(sym): #takes only the symptom as input, and displays a medicine for it. This function is only for when the user inputs a single syMptom ONLY.

	if sym=="1":
		print("Suggested medicine: Disprin.")

	elif sym=="2":
		print("Suggested medicine: Clozapine.")

	elif sym=="3":
		print("Suggested medicine: Black Cohosh")

	elif sym=="4":
		print("Suggested medicine: Ethextrol")

	elif sym=="5":
		print("Suggested medicine: Tea Tree Oil")

	elif sym=="6":
		print("Suggested medicine: Tylenol")

	elif sym=="7":
		print("Suggested medicine: Visine")

	elif sym=="8":
		print("Suggested medicine: Phenergan")

	elif sym=="9":
		print("Suggested medicine: Meclizine")

	elif sym=="10":
		print("Suggested medicine: Acetaminophen")

	elif sym=="11":
		print("Suggested medicine: Visine Eyes drops")

	elif sym=="12":
		print("Suggested medicine: Ibuprofen")

def disease(sym): #takes multiple symptoms and tells the patient the diseases that he could possibly have, and suggests a medicine for them as well. Asks further questions, to shortlist a particular disease.

	disease= "No disease could be evaluated."
	for i in range(len(sym)):

		sym01= sym[i]

		if sym01=="1":

			ques01= input("Have you been to a place of high altitude recently? Answer with yes or no :")
			
			if ques01=="yes":

				print("You could have altitude sickness.")
				disease= "altitude sickness"  #this value of "disease" variable will be passed onto the medication function at the end of this loop, to suggest a medicine.

			elif ques01=="no":
				diseaseFound= False

				for a in range(len(sym)):

					if sym[a]=="9":

						print("You are suffering from hypertension.")
						disease= "hypertension"
						diseaseFound=True
						break

				if diseaseFound==True:
					continue

				else:
					
					ques02= input("Have you been suffering from flu-like symptoms like coughs, fever, sore throat,etc ? yes/no :")

					if ques02=="yes":

						print("You might have HIV.")
						disease="HIV"


					elif ques02=="no":

						print("You're suffering from a simple headache.")
						disease= "headache"


		elif sym01=="2":

			ques01= input("Do you also laugh or cry involuntarily and without any reason? yes/no: ")

			if ques01== "yes":

				print("You might have Alzheimer's disease.")
				disease= "alzheimer"


			elif ques01=="no":

				print("No disease found based on your symptom no.2 found.")

		elif sym01=="3":

			ques01= input("Do you sweat ONLY at night? yes/no :")

			if ques01== "yes":

				ques02= input("Do you also have trouble breathing? yes/no : ")
				
				if ques02=="yes":

					print("You could be suffering from arthritis. ")
					disease= "arthritis"


				else:

					print("Couldn't find a disease matching your symptom no. 3.")

			elif ques01=="no":	

				for i in range(len(sym)):

					if sym[i]=="8":

						print("You could have myocardia infarction.")
						disease= "myocardial infarction"
						break


		elif sym01=="4":

			ques01= input("Do you have trouble breathing or suffer from temporary cardia arrests? yes/no : ")

			if ques01=="yes":

				print("You have asthma.")
				disease= "asthma"


			else:

				print("Couldn't find any disease matching symptom 4.")

		elif sym01=="5":

			print("You could be suffering from Alopecia.")
			disease= "alopecia"


		elif sym01=="6":

			ques01=input("Do you have difficulty urinating as well? yes/no : ")

			if ques01=="yes":

				print("You could have bladder cancer. ")
				disease="bladdercancer"


			else:

				print("Coulnd't find a disease matching symptom no. 6. You must simply be exhausted.")

		elif sym01=="7":

			for a in range(len(sym)):

				if sym[a]=="8":
					
					print("You could have brain tumor.")
					disease="braintumor"
					break

				else:

					print("No diseases matching your symptom no. 7. You must simply be feeling weak.")
					break

		elif sym01=="8":

			for a in range(len(sym)):

				diseaseFound=False

				if sym[a]=="9":

					print("You are dehydrated.")
					disease="dehydration"
					diseaseFound=True
					break

				elif sym[a]=="12":

					print("You could be suffering from hepatitis.")
					disease="hepatitis"
					diseaseFound=True
					break

			if diseaseFound==False:
				print("No disease matching symptom no 8 found.")

		elif sym01=="9":

			ques01= input("Do you also have trouble breathing? yes/no : ")

			if ques01=="yes":

				ques02= input("Do you also have irregular or a very strong heart beatat some times? yes/no : ")

				if ques02=="yes":

					print("You could be suffering from Cardiovascular disease.")
					disease="cardiovascular"


				elif ques02=="no":

					print("You could be suffering from a heart failure.")
					disease="heartfailure"


			else:
				
				print("No diseases matching your symptom no.9 found. You must simply be feeling weak.")

		elif sym01=="10":

			print("You have dermatitis.")
			disease="dermatitis"


		elif sym01=="11":

			ques01= input("Do you also have either watery eyes or fever? yes/no: ")

			if ques01=="yes":

				print("You have Influenza.")
				disease="influenza"


			else:

				print("No disease matching your symptom no. 11 found. ")

		elif sym01=="12":

			diseaseFound=False

			for a in range(len(sym)):

				if sym[a]=="13":

					print("You could be suffering from leukemia.")
					disease="leukemia"
					diseaseFound=True
					break

			if diseaseFound==False:

				print("No disease matching your symptom no.12 was found.")

		medication(disease)

def main():

	resp01= input("Do you wish to enter more than one symptoms? yes/no : ")

	if resp01=="yes":

		sym= input("Enter the numbers for the symptoms you have: ").split()
		disease(sym)

	else:

		sym=input("Enter the number for the symptom you have: ")
		simpleMed(sym)

main()