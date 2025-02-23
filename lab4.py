counter1 = 0
counter2 = 0
aString = "The purpose of this program assignment is to practice how to use for loop and if-else statement."

print("The String is" + aString)
print("")
print("")

for index in range(len(aString)):
    if aString[index] == 'o':
        print("'o' character occurs in index:" + str(index))
        counter1 = counter1 + 1
print("There are " + str(counter1) + " of 'o's in a string")
print("************************************************************")
print()

for index in range(len(aString)):
    if aString[index] == 's':
        print("'s' character occurs in index:" + str(index))
        counter2 = counter2 + 1
print("There are " + str(counter1) + " of 's's in a string")
print("************************************************************")
print("There are " + str(len(aString)) + " characters in the string.")
