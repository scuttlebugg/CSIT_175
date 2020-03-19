print("Assignment 3\n")

userName = input("Please enter your name: ")
print()

#best friends list
outputBesties = "\nMy friends are:\n"
for count in range(3):
    friendName = input("Please enter the names of your 3 best friends: ")
    count += 1
    outputBesties += str(count) + ". " + friendName + "\n"
print(outputBesties)

#guest list
print("Enter the names of other people attending your wedding.\n ")
outputGuests = "\nMy wedding attendees are:\n"
i = 0
guestName = True
while guestName != "":
    guestName = input("Guest name (or press Enter to quit): ")
    i += 1
    if len(guestName) > 0:
        outputGuests += str(i) + ". " + guestName + "\n"
print(outputGuests)
print("END OF ASSIGNMENT 3")
