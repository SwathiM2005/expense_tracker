import os

def add_expenses():
    category=input("Enter the category:")
    amount=float(input("Enter the amount spent:"))
    description=input("Enter the details:")
    with open("expenses.txt","a")as file:
        file.write(f"{category},{amount},{description}\n")
    print("The expenses are added:")

def view_expenses():
    if not os.path.exists("expenses.txt"):
        print("No expenses recorded yet.\n")
        return

    with open("expenses.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No expenses recorded yet.\n")
            return

        # Print table header
        print(f"{'Category':<15}{'Amount':<10}{'Description':<30}")
        print("="*55)

        # Print each expense in a row
        for line in lines:
            category, amount, description = line.strip().split(",")
            print(f"{category:<15}{amount:<10}{description:<30}")

            
while True:
    print("___The expenser tracker____")
    print("1->add the expense")
    print("2-> View Expense")
    print("3->quit")
    choice=input("Enter the choice:").strip()

    if choice=="1":
        add_expenses()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        print("exiting expense tracker,Come back again later")
        break
    else:
        print("Invalid choice")

