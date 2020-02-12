#title of program
print("...Super-Fancy Sleep Calculator Program...\n")

#gather information from user
userName = input("Please enter your name: ")
userAge = int(input("Please enter your age: "))
nightlySleep = int(input("On average, how many hours do you sleep each night? "))

#calculate how many hours of sleep over lifetime
wastedYears = round((nightlySleep/24) * userAge,2)

#output total to console
print()
print("Hello, " + userName)
print("You have been unconscious for " + str(wastedYears) + " years. Oh my!")

    
