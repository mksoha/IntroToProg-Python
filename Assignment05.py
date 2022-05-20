# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Using Lists & Dictionaries
#              When the program starts, load each "row" of data
#              in "ToDoToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot, 1.1.2030, Created starter script
# Michael Soha, Due: May 17, 2022, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# | Declare variables and constants | #

objFileName = "ToDoList.txt"  # Object that represents a file
strData = ""  # Row of text data from the file
dicRow = {}  # Row of data separated into elements of a dictionary
lstTable = []  # Dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection

# Step 1 | When the program starts, load from ToDoList.txt into a python dictionary

objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Step 2 | Display a menu of choices to the user

while True:
    print("""
    Menu of Options
    1) Show Current Data
    2) Add a New Item
    3) Remove an Existing Item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()

# Step 3 | Show the current items in the table
# Selection '1'

    if strChoice.strip() == '1':
        print("******* The Current Items ToDo Are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

# Step 4 | Add a new item to the table
# Selection '2'

    elif strChoice.strip() == '2':
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data In Table:")

        # Step 4(a) | Show the current items in the table

        print("******* The Current Items ToDo Are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

# Step 5 | Remove a new item to the table
# Selection '3'

    elif strChoice == '3':

        # Step 5(a) | Allow user to indicate which row to delete

        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
            # end if
        # end for loop
        # Step 5 (b) | Update user on the status
        if blnItemRemoved:
            print("The task was removed.")
        else:
            print("Task could not be found.")

        # Step 5(c) | Show the current items in the table

        print("******* The Current Items ToDo Are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue  # to show the menu

# Step 6 | Save tasks to the ToDoFile.txt file
# Selection '4'

    elif strChoice == '4':

        # Step 6(a) | Show the current items in the table

        print("******* The Current Items ToDo Are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

        # Step 6(b) | Ask if they want save that data

        if "y" == str(input("Save this data to file? (y/n) - ")).strip().lower():
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

# Step 7 | Exit program
# Selection '5'

    elif strChoice == '5':
        break  # and EXIT the program
