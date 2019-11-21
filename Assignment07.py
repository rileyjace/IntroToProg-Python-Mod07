# ------------------------------------------------- #
# Title: Lab7-1
# Description: Assignment 07 - Pickling and Error Handling
# ChangeLog: (Who, When, What)
# <JRiley>,<11.18.2019>,Created Script
# <JRiley>,<11.18.2019>,Updated Script
# ------------------------------------------------- #

import pickle # importing a code from another code file. This is used in the Demonstrate Pickling section.

# ____________________________________________________________________________________________________#
# Demonstration for Error Handling within Python 3.X
# _____________________________________________________________________________________________________#

def divide():
    x = float(input("Enter a value to divide: "))
    y = float(input("Enter a value to divide by: "))
    result = x//y
    print ("The answer is: ", result)

# Demonstrate a generic try and except handling of an error
try:
    divide()
except:
    print("An exception occurred.")

# Demonstrate an error with a specific error

print("\nEnter a zero as your second number.\n")
try:
    divide()
except ZeroDivisionError:
    print("Sorry! You are dividing by zero.\n")
except:
    print("Something else went wrong.\n")


# Demonstrate an error utilizing finally

print("Press enter instead of one of your numbers it is requesting below.\n")
try:
    divide()
except ZeroDivisionError:
    print("Sorry! You are dividing by zero.")
except:
    print("Something else went wrong.")
finally:
    print("The 'try except' is finished.")

# ____________________________________________________________________________________________________#
# Demonstrate Pickling
# ____________________________________________________________________________________________________#


# Data
fileName = "HomeInventory.dat"
itemList = []

# Processing
def enterData():
    print('Type in a "Name" and value for your household items')
    try:
        name = str(input('Enter an Item Name: '))
    except:
        print("Sorry, incorrect entry type, please enter a string as the item.")
    try:
        value = int(input('Enter a Value: '))
    except ValueError:
        print("Sorry, incorrect entry type, please enter a integer value.")
    itemList.append(name + ', $' + str(value))
    print(itemList)

def readData():
    objFile = open(fileName, "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    print(list_of_data)

def saveData():
    print('Would you like to save your Data?')
    # Input is cast as a variable to allow for option to save or not.
    prompt = input('Enter "y" or "n"')
    if prompt.lower() == 'y':
        print('saving data to file...')
        file = open("HomeInventory.dat", "wb")
        pickle.dump(itemList, file)
        file.close()
    else:
        print('You have exited without saving')

# Demonstration
while True:

    # The print statement gives the options to the user.
    print('\n' + 'Please enter from these menu options:' + '\n' + '1) Add Data to List' + '\n' +
          "2) Display Current Data" + '\n' + '3) Save to File' + '\n'+ '4) Exit' + '\n')
    # Casting the input as a variable to allow it to be used through the options given.

    option = input('Which option would you like to perform? (1 to 4): ')

    # Option 1 is to append the name and value entered by the user into the in memory list.
    if option == '1':
        enterData()

    # Option 2 is to give the user back the information for review to see if they want to save with option 3.
    elif option == '2':
        readData()

    # Option 3 is to allow the user to either save the data to a text file or exit without saving.
    elif option == '3':
        saveData()
    elif option == '4':
        print("You have exited the program")
        break