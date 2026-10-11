#Declaration
from copy import replace
main_expense = {}

#Methods
#Method-1
def User_Choice():
    user_choice = int(input("1.)Add Expense\n2.)Update Expense\n3.)Delete Expense\n4.)View Expense\n5.)View Summary of Expenses\n6.)Exit\nEnter your choise here:"))
    return user_choice

#Method-2:
def add_expense():
    print("User choose:Add Expense")
    expense_01={}
    no_of_expense = int(input("Enter number of Expense(s) you want to add:"))
    for i in range(no_of_expense):
        expense_name = input("Enter your Expense name here:")
        expense_amount = int(input("Enter your Expense Amount here:"))
        expense_01[expense_name] = expense_amount
    print(expense_01)
    #Updating the main expense dictionary from expense(expense_01) dictionary
    main_expense.update(expense_01)

    #File operations
    with open("your_expense.txt",mode="a",encoding="utf-8") as add_expense_file:
        for name, amount in expense_01.items():
            add_expense_file.write(f"Expense :{name} | Amount:{amount}\n")

    print(f"Expense(s) added successfully")
    
    choice_01_01 = input("Enter 'Y' or 'y' to add more Expense(s) or 'N' or 'n' to exit:")    
    if(choice_01_01.lower()=="y"):
        add_expense()

#Method-3:
def update_expense():
    print("User Choose : Update Expense")
    find_expense = input("Enter the Expense Below to Update :")
    #find_expense is a key in main_expense dictionary
    if(find_expense in main_expense):           
        print("Expense found")
        update_choice = int(input("Enter '1' to update Expense name or '2' to update Expense amount :"))

        #Step-1:We add try and except block
        #Step-2:in try block ,we opened the file in read mode
        #Step-3:We created lines(variable)and update_expense_file(file variable) and used readlines() method
        #Step-4:close the file
        #Step-5:in except block, we will print "File not found" and create empty list for lines
        try:
            with open("your_expense.txt",mode="r",encoding="utf-8") as update_expense_file:
                lines = update_expense_file.readlines()
                update_expense_file.close()
        except FileNotFoundError:
            print("File not found")
            lines = []

        if(update_choice==1):
            new_expense_name = input("Enter new Expense name to update:")
            #It will remove find_expense from main_expense and will put new_expense_name to main_expense 
            #with the same value as find_expense had earlier
            main_expense[new_expense_name] = main_expense.pop(find_expense)                
            print(f"Updation done successfully\nUser updated \"{find_expense}\" to \"{new_expense_name}\"")
            print(f"Updated list is {main_expense}")

            old_line_start = f"Expense :{find_expense}"
            
        elif(update_choice==2):
            new_expense_amount = int(input("Enter new Expense amount to update:"))
            main_expense[find_expense] = new_expense_amount
            print(f"Updation done successfully\nUser updated \"{main_expense[find_expense]}\" to \"{new_expense_amount}\"")
            print(f"Updated list is {main_expense}")
        else:
            print("Invalid Choice")
    
    choice_02_01 = input("Enter 'Y' or 'y' to update Expense(s) or 'N' or 'n' to exit:")    
    if(choice_02_01.lower()=="y"):
        update_expense()
        
#Method-4
def delete_expense():
    print("User Choose : Delete Expense")
    delete_choice = input("Enter the Expense you want to delete:")
    if(delete_choice in main_expense):
        del main_expense[delete_choice]
        print(f"Expense \"{delete_choice}\" deleted successfully")
        print(f"Updated list is {main_expense}")
    
    choice_03_01 = input("Enter 'Y' or 'y' to delete Expense(s) or 'N' or 'n' to exit:")    
    if(choice_03_01.lower()=="y"):
        delete_expense()

#Method-5
def view_expense():
    print("User Choose : View Expense")
    view_choice = input("Enter the Expense to view:")
    if(view_choice in main_expense):
        print("Expense found")
        print(f"Expense is {view_choice} and Expense amount is {main_expense[view_choice]}")
    else:
        print("Expense not found")

    choice_04_01 = input("Enter 'Y' or 'y' to view Expense(s) or 'N' or 'n' to exit:")    
    if(choice_04_01.lower()=="y"):
        view_expense()

#Method-6
def expense_summary():
    print("View Summary of Expenses")
    print(main_expense)

#Method-7
def exit_program():
    print("Exit")

    

#Main Program
while True:
    print("EXPENSE TRACKER")
    print("Enter what activity you want to do:")
    choice_01 = User_Choice()
    if(choice_01==1):
        add_expense()
    elif(choice_01==2):
        update_expense()
    elif(choice_01==3):
        delete_expense()
    elif(choice_01==4):
        view_expense()
    elif(choice_01==5):
        expense_summary()
    elif(choice_01==6):
        exit_program()
        break
    else:
        print("Invalid choice")



