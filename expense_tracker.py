def add_an_expense():
    expense_amount = input('Enter the amount: ')
    expense_category = input("Enter the expense category: ")
    if expense_category in Expense_list:
        Expense_list[expense_category].append(expense_amount)
    else:
        Expense_list[expense_category] = [expense_amount]
    print("Expense added successfully")

choice = input("Enter your choice: ")
if choice == "1":
    add_an_expense()
elif choice == "2":
    search_by_category()
elif choice == "3":
    exit()
else: None

def search_by_category():
    search_choice = input("Category: ")
    if search_choice in Expense_list:
        print("Category found!")
        expenses = Expense_list[search_choice]
        total_expense = sum(map(int, expenses))
        print("Total expense in", search_choice, ":", total_expense)
    else: print("Category not found")

while 1 == True:
    print("Expense Tracker Program")
    print("-----------------------")
    print("1. Add an expense")
    print("2. Search for expenses by category")
    print("3. Exit")

    Expense_list = {}

    choice = input("Enter your choice: ")
    if choice == "1":
        add_an_expense()
    elif choice == "2":
        search_by_category()
    elif choice == "3":
        exit()
    else: None





