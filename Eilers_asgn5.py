import random

def displayMyClasses(classList):
    """
    sorts classes and prints them in a decending numerical list
    accepts list of classes
    returns noting because lists are mutable
    """
    classList.sort(key=str.lower)
    count = 1
    for item in classList:
        print(str(count) + ". " + item)
        count += 1

def guessNext(classList):
    """
    accepts list of classes
    returns random item from class list
    """
    return random.choice(classList)
    
def main():
    classList = ['Python', 'JavaScript', 'PHP'] #set initial class list
    print("ASSIGNMENT 5\n")
    displayMyClasses(classList)
    #loop for add or remove class, blank to end loop
    while True:
        userSelection = input("\nEnter A to add a new class or enter an R to remove a class: ")
        if userSelection.lower() == "a":
            addClass = input("\nEnter the class you wish to add: ")
            classList.append(addClass)
            continue
        elif userSelection.lower() == "r":
            removeClass = input("\nEnter the class you wish to remove: ")
            classList.remove(removeClass)
            continue
        elif userSelection == "":
            break
        else:
            print("\nYou must choose either A to add or R to remove a class.")
            continue

    displayMyClasses(classList)
    randomSelection = guessNext(classList)
    print("\nYou should teach", randomSelection)
    print("\nEND OF ASSIGNMENT 5")

if __name__ == "__main__":
    main()
