"""
- You’ll simulate tracking your expenses for 7 days. Each day, the user will enter multiple expenses (food, travel, etc.) as numbers. At the end:

You'll store daily totals in a list

Then convert that list into a tuple (to lock it from editing)

- You’ll display:

Total spent in the week

Highest and lowest spending day

Number of days where spending was zero

Position of the highest spending day (index)

- 💻 Features to Implement
Daily Input (List of lists)
Example:
[[120, 50], [0], [100, 100, 50], …]
Use nested lists to store multiple entries per day.

Convert to Daily Totals List
[170, 0, 250, …]
Sum each day's entries.

Convert Daily Totals to Tuple
Use a tuple to show immutability.

Display Summary

Total spending in the week

Highest spending = max()

Lowest spending = min()

Days with 0 spending = count(0)

Day index of highest spending = index(max(...))


"""


# Personal Expense Tracker – Weekly Summary Using Lists & Tuples (Safe Input Version)

print("📒 Welcome to Weekly Expense Tracker 💰")
print("Enter your daily expenses for 7 days.")
print("Note: Use spaces to separate numbers. Don't use commas.\n")

# Step 1: Collect daily expenses safely
weekly_expenses = []

for day in range(1, 8):
    while True:
        daily_input = input(f"Enter your expenses for Day {day} (e.g., 120 50 30): ")
        
        # Replace commas with spaces to sanitize input
        cleaned_input = daily_input.replace(",", " ").strip().split()
        
        try:
            # Convert each item to integer
            expenses = list(map(int, cleaned_input))
            weekly_expenses.append(expenses)
            break  # Exit the loop if input is valid
        except ValueError:
            print("❌ Invalid input. Please enter only numbers separated by spaces. Example: 100 50 20")

# Step 2: Display daily input summary
print("\n✅ Your daily expenses:")
for i, day_exp in enumerate(weekly_expenses, start=1):
    print(f"Day {i}: {day_exp}")

# Step 3: Convert daily expenses to daily totals
daily_totals = [sum(day) for day in weekly_expenses]
print("\n💡 Daily totals (list):", daily_totals)

# Step 4: Convert daily totals to a tuple (to show immutability)
weekly_summary = tuple(daily_totals)
print("🔐 Weekly summary (tuple):", weekly_summary)

# Step 5: Summary calculations
total_spent = sum(weekly_summary)
highest_spending = max(weekly_summary)
lowest_spending = min(weekly_summary)
zero_spending_days = weekly_summary.count(0)
index_highest_day = weekly_summary.index(highest_spending)

# Step 6: Display final summary
print("\n📊 Weekly Summary:")
print(f"📅 Total spent in the week: ₹{total_spent}")
print(f"💸 Highest single-day spending: ₹{highest_spending}")
print(f"🧾 Lowest single-day spending: ₹{lowest_spending}")
print(f"📉 Days with zero spending: {zero_spending_days}")
print(f"🏆 Day with highest spending: Day {index_highest_day + 1}")

# Step 7: Show tuple immutability
print("\n🔒 Demonstrating that tuples are immutable:")
try:
    weekly_summary[0] = 999
except TypeError as e:
    print("❌ Error:", e)
