# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# RRoot,1.1.2030,Created started script
# Ahson Butt,11/17/20, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open('ToDoList.txt', 'r')
        for row in objFile:
            dicRow = row.split(',')
            print(dicRow[0] + '|' + dicRow[1].strip())
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        objFile = open('ToDoList.txt', 'a')
        strt = input('What is your Task: ')
        strp = input('and your Priority: ')
        dicRow = {'Task': strt, 'Priority': strp}
        objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        objFile = open('ToDoList.txt', 'r+')
        task = input("Delete: ")
        if task in objFile:
            del objFile[task] #I can't get this part to work...
        else:
            print("Term not in Dictionary") #my script is not recognizing the data in the file, why?
        objFile.close()

    # Step 6 - Save tasks to the ToDoToDoList.t  xt file
    elif (strChoice.strip() == '4'):
        ObjFile = open('ToDoList.txt', 'r')
        print('File will be saved')
        objFile.close() #I don't understand how this is different from selection 2
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break
