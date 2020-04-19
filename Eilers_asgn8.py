def main():
    # declare empty dictionary and list
    dictionary = {}
    firstName = []
    
    with open("A8_names.txt", "r") as file:
        for line in file:
            fname = line.strip().split("*")[0]
            lname = line.strip().split("*")[1]
            dictionary[fname] = lname

    firstList = list(dictionary.keys())
    firstList.sort()
    
    while True:
        # ask user for input
        userInput = input("\nWhat is the first name you are looking for? ")
        print()
        userInput = userInput.title() # pronoun capitalization

        if userInput == "":
            exit()
        elif userInput in dictionary:
            print()
            print("The full name is: " + userInput + " " + dictionary[userInput])
        else:
            print()
            print("I was unable to find " + userInput + " in the list. ")
    
    print("\n\nEnd of program.")
    

if __name__ == "__main__":
    main()
