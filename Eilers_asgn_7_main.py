import Eilers_asgn_7_module as module
import datetime

def main():
    print("* * The Wizard * *\n")
    print("The Wizard will see you now")
    
    payMe = module.payMe()
    if payMe == False:
        print("Go away!")
        exit()
    
    while True:
        userName = input("\nWhat is your name? ")
        if userName == "":
            continue
        else:
            break
    while True:
        question = input("\nWhat is your question? ")
        if question == "":
            continue
        else:
            
            magicWord = module.getTarget(question)
            displayList = module.createList(magicWord)
            wizardMessage = module.spinWheel(userName, displayList)

            print("\nAttention, " + userName + "! The Wizard declares: " + wizardMessage)
            anotherQuestion = input("\nDo you have another question? (Y/N) ")
            if anotherQuestion.lower() == "y":
                continue
            else:
                break
    dtnow = datetime.datetime.now()
    month = dtnow.strftime("%B")
    weekday = dtnow.strftime("%A")
    date = str(dtnow.day)
    year = str(dtnow.year)
    print("\nOn this day, " + weekday + ", the " + date + "th" + " of " + month + " in the year of " + year)
    print("The Wizard wants you to go away now!")

if __name__ == "__main__":
    main()
