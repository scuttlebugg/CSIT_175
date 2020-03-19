import asgn4_module as module

def getFirstName():
    """
    accepts no arguments
    returns a string for user first name
    """
    blank = True
    while blank == True:
        string = input("\nWhat is your first name? ")
        blank = module.is_field_blank(string)
        if blank == True:
            print("First name must be entered. ")
        else:
            return string


def getLastName():
    """
    accepts no arguments
    returns a string for user last name
    """
    blank = True
    while blank == True:
        string = input("\nWhat is your last name? ")
        blank = module.is_field_blank(string)
        if blank == True:
            print("Last name must be entered. ")
        else:
            return string

def getAge():
    """
    accepts no arguments
    returns a integer value for user age input
    """
    blank = True
    while blank == True:
        number = input("\nWhat is your age? ")
        blank = module.is_field_blank(number)
        if blank == True:
            print("Age must be entered. ")

    num = False
    while num == False:
        num = module.is_field_a_number(number)
        if num == False:
            print("Age must be a number. ")
            number = input("\nWhat is your age? ")
        else:
            return int(number)


def finalMessage(firstName, lastName, age):
    """
    accepts no 2 strings and an int from user input
    returns no value. Prints greeting and judgement
    of user age if over 40
    """
    if age > 40:
        print("\nWell,", firstName, lastName, ", it looks like you are over the hill!")
    else:
        print("\nHello,", firstName, lastName)

def main():
    print("Assignment 4\n")
    firstName = getFirstName()
    lastName = getLastName()
    age = getAge()
    finalMessage(firstName, lastName, age)
    print("\nEND OF ASSIGNMENT 4")

if __name__ == "__main__":
    main()
