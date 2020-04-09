import datetime

def payMe():
    """
    accepts no parameters
    returns boolean value. Handles errors and exceptions for money value
    Determines if payment is enough to be worth Wizard's time
    """
    print("What's the most you are willing to pay me for my advice? ")
    try:
        payment = float(input("\nThe more you pay, the better the answer! (minimum price: $975.46) "))

    except Exception:
        print("\nHmm... Something seems to have gone wrong. \nWhy don't you restart and try again?")
        exit()

    if payment < 975.46:
        return False
    if payment >= 975.46:
        print("\nI guess", "{:,.2f}".format(payment), "seems like a fair price... ")
        return True


def getTarget(question):
    """
    accepts question input by user
    returns key word value.
    """
    if "who" in question.lower():
        return "who"
    if "what" in question.lower():
        return "what"
    if "where" in question.lower():
        return "where"
    if "when" in question.lower():
        return "when"
    if "why" in question.lower():
        return "why"
    if "how" in question.lower():
        return "how"
    else:
        return "unknown"


def createList(magicWord):
    """
    accepts magic word string value
    returns displayList with keyword specific answers
    reads from Oracle file and splits each line into 2 lists
    """
    displayList = []
    keyword = []
    answerList = []
    holdList = []

    with open("A7_answers.txt", "r") as file:
        for line in file:
            keyword.append(line.strip().split("*")[0])
            answerList.append(line.strip().split("*")[1])
            i = 0
        for item in keyword:
            if magicWord.lower() in keyword[i].lower():
                displayList.append(answerList[i])
            i += 1  
    return displayList


def spinWheel(userName, displayList):
    """
    accepts user name and disply list
    returns displayList item with remainder index value
    randomly chooses answer from displaylist based on time
    """
    num = len(displayList)
    if num <= 0:
        remainder = 0
    else:
        dtnow = datetime.datetime.now()
        remainder = ((dtnow.second) % num)
    while True:
        print("\nPress Enter to Spin the Wheel")
        pressEnter = input()
        if pressEnter == "":
            print("\nSpin..Spin..Spin....Spin.......Spin........tick, tick, tick, stop")
            break
        else:
            continue
    return displayList[remainder]
            
