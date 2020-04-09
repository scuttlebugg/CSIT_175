import os


fileName = "items.txt"


def userInput():
    """
    accepts no arguments
    asks for file name input
    returns no value
    """    
    while True:
        try:
            userEntry = input("Please enter a file name: ")
            if userEntry == "end":
                    exit()
            with open(userEntry) as file:
                if userEntry.lower() == fileName:
                    break
        except FileNotFoundError:
            print("File not found. Please try again.\n")

            
def importFileToList(f):
    """
    accepts file as argument
    asks for file name input
    returns filled list without \n
    """
    with open(f) as file:
        res = []
        for line in file:
            res.append(line.strip())
        return res
        

def sortList(l):
    """
    accepts list as argument
    sorts list alphabetically
    returns sorted list
    """
    l.sort(key=str.lower)
    return l


def getPrices(l):
    """
    accepts list as argument
    asks user for input prices, tests for numeric value, writes to txt file
    calls print function within to print txt file contents
    returns nothing
    """
    i = 0
    costList = []
    with open("costlist.txt", "a") as file:
        file.write("\nCost List:\n\n")
        for item in l:
            costEntry = input("How much are " + l[i] + "? ")
            try:
                cost = float(costEntry)
                costList.append(float(cost))
                file.write(str(l[i]) + " cost " + str(costList[i]) + " dollars.\n")
            except ValueError:
                    print("You have entered an invalid float. " + costEntry + " could not be converted to a float.", end="")
                    print("\nSkipping to he next item after " + l[i] + ".")
                    costList.append("\n")
            i += 1
    printPrices()


def printPrices():
    """
    accepts no arguments
    opens file and prints contents
    returns nothing
    """
    with open("costlist.txt", "r") as file:
        contents = file.read()
        print(contents)
    

def main():
    if os.path.exists("costlist.txt"):
        os.remove("costlist.txt")
    print("ASSIGNMENT 6\n")
    userInput() #get text file name
    myList = importFileToList(fileName) #bring in data from file into myList
    myList = sortList(myList) #sort list alphabetically
    getPrices(myList) #append prices to list
    print("Program End")
    

if __name__ == "__main__":
    main()
