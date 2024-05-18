import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Initialize an empty DataFrame to store expenses
        self.expenses = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

    def add_expense(self, date, category, amount, description):
        # Create a new expense entry as a DataFrame
        new_expense = pd.DataFrame({
            "Date": [date],
            "Category": [category],
            "Amount": [amount],
            "Description": [description]
        })
        # Append the new expense to the DataFrame using pd.concat
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        print("Expense added successfully.")

    def view_expenses(self):
        # Check if there are any expenses recorded
        if self.expenses.empty:
            print("No expenses recorded yet.")
        else:
            # Print the DataFrame of expenses
            print(self.expenses)

    def get_summary(self):
        # Check if there are any expenses to summarize
        if self.expenses.empty:
            print("No expenses to summarize.")
        else:
            # Group expenses by category and sum the amounts
            summary = self.expenses.groupby("Category")["Amount"].sum().reset_index()
            print("\nSummary by Category:")
            print(summary)

    def run(self):
        # Infinite loop for the command-line interface
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Get Summary")
            print("4. Exit")

            # Get user choice
            choice = input("Choose an option: ")

            if choice == '1':
                # Add an expense
                date = input("Enter the date (YYYY-MM-DD): ")
                try:
                    # Validate the date format
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please try again.")
                    continue

                category = input("Enter the category: ")
                try:
                    # Validate the amount input
                    amount = float(input("Enter the amount: "))
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    continue
                description = input("Enter the description: ")

                # Add the expense to the tracker
                self.add_expense(date, category, amount, description)

            elif choice == '2':
                # View all expenses
                self.view_expenses()

            elif choice == '3':
                # Get summary by category
                self.get_summary()

            elif choice == '4':
                # Exit the program
                print("Exiting the Expense Tracker.")
                break

            else:
                print("Invalid choice. Please try again.")

# Main execution block
if __name__ == "__main__":
    # Create an instance of ExpenseTracker
    tracker = ExpenseTracker()
    # Run the command-line interface
    tracker.run()
