print("Assignment 2\n")
userName = input("What is your name? ")

#The name and greeting debaucle
if userName == "":
    userName = input("\nPlease Enter your name ")
    if userName == "":
        print("Name is missing, exiting program\n\n")
        exit()
if userName.lower() == "steve":
    print("\nYou are the instructor")
else:
    print("\nHi " + userName + " You are a student")

#Get user birth year
userBirthYear = input("What year were you born? ")
if userBirthYear.isnumeric():
    #Get user location
    userCity = input("What city do you live in? ")
    if userCity.lower() == "fresno" or userCity.lower() == "bakersfield":
        print("I'm sorry it's so hot where you live.")
    else:
        print("\nHope you like it in", userCity)
if not(userBirthYear.isnumeric()):
    userBirthYear = input("\nPlease enter your birth year with all numbers: ")
if userBirthYear == "":
    print("You never told me when you were born!")
print("It must be a good life for people born in", userBirthYear)
print("END OF ASSIGNMENT 2")
