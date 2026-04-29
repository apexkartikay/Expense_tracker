import json
from datetime import datetime

FILE = "expenses.json"

# ---------------- FILE HANDLING ----------------
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- ADD EXPENSE ----------------
def add_expense(data):
    try:
        amount = float(input("Enter amount: "))
        category = input("Category (food/travel/shop/etc): ")
        note = input("Note: ")
        date = datetime.now().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        }

        data.append(expense)
        save_data(data)
        print(" Expense added!")

    except:
        print(" Invalid input!")

# ---------------- VIEW ----------------
def view_expenses(data):
    if not data:
        print("No expenses yet.")
        return

    for i, e in enumerate(data):
        print(f"{i+1}. ₹{e['amount']} | {e['category']} | {e['note']} | {e['date']}")

# ---------------- SUMMARY ----------------
def monthly_summary(data):
    month = input("Enter month (YYYY-MM): ")
    total = 0

    for e in data:
        if e["date"].startswith(month):
            total += e["amount"]

    print(f" Total spending in {month}: ₹{total}")

# ---------------- CATEGORY ----------------
def category_summary(data):
    summary = {}

    for e in data:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    for k, v in summary.items():
        print(f"{k}: ₹{v}")

# ---------------- HIGHEST ----------------
def highest_expense(data):
    if not data:
        print("No data")
        return

    high = max(data, key=lambda x: x["amount"])
    print(" Highest Expense:", high)

# ---------------- SEARCH ----------------
def search(data):
    key = input("Enter keyword: ")
    for e in data:
        if key.lower() in e["category"].lower() or key.lower() in e["note"].lower():
            print(e)

# ---------------- DELETE ----------------
def delete_expense(data):
    view_expenses(data)
    try:
        idx = int(input("Enter index to delete: ")) - 1
        removed = data.pop(idx)
        save_data(data)
        print("🗑️ Deleted:", removed)
    except:
        print("Invalid choice")

# ---------------- BUDGET ----------------
def budget_alert(data):
    limit = float(input("Enter monthly budget: "))
    month = datetime.now().strftime("%Y-%m")

    total = sum(e["amount"] for e in data if e["date"].startswith(month))

    print(f"Spent this month: ₹{total}")

    if total > limit:
        print(" Budget exceeded!")
    else:
        print(" Within budget")

# ---------------- MAIN ----------------
def main():
    data = load_data()

    while True:
        print("\n====  EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Highest Expense")
        print("6. Search")
        print("7. Delete Expense")
        print("8. Budget Check")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            monthly_summary(data)
        elif choice == "4":
            category_summary(data)
        elif choice == "5":
            highest_expense(data)
        elif choice == "6":
            search(data)
        elif choice == "7":
            delete_expense(data)
        elif choice == "8":
            budget_alert(data)
        elif choice == "9":
            print(" Bye!")
            break
        else:
            print("Invalid option")

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
