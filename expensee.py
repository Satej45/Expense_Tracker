import csv
from datetime import datetime
import matplotlib

matplotlib.use('TkAgg')  # or 'Qt5Agg' depending on your system
import matplotlib.pyplot as plt
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def record_expense(self, amount, category):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses.append({'timestamp': timestamp, 'amount': amount, 'category': category})
        print("Expense recorded successfully.")

    def view_spending_over_time(self):
        timestamps = [expense['timestamp'] for expense in self.expenses]
        amounts = [expense['amount'] for expense in self.expenses]
        dates = [datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") for timestamp in timestamps]

        plt.plot(dates, amounts, marker='o')
        plt.title('Spending Over Time')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.show()

    def save_to_csv(self, filename='expenses.csv'):
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['timestamp', 'amount', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(self.expenses)
        print(f"Expenses saved to {filename}.")

    def load_from_csv(self, filename='expenses.csv'):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.expenses = [row for row in reader]
            print(f"Expenses loaded from {filename}.")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty list.")

def main():
    tracker = ExpenseTracker()
    tracker.load_from_csv()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Record Expense")
        print("2. View Spending Over Time")
        print("3. Save Expenses to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            tracker.record_expense(amount, category)
        elif choice == '2':
            tracker.view_spending_over_time()
        elif choice == '3':
            tracker.save_to_csv()
        elif choice == '4':
            tracker.save_to_csv()
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
