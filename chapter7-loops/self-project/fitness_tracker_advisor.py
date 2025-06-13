"""
Problem Statement:
You're building a basic fitness tracker that gives advice based on a user's daily step count.

✅ Inputs to take from user:
steps → (an integer, the number of steps walked today)

⚙️ Conditions:
Steps Range	Output / Advice
Less than 1000	"Too little movement. Try a short walk!"
1000 to 4999	"Good start! Try to move more today."
5000 to 9999	"Nice job! You're staying active."
10000 or more	"Excellent! You've reached your goal!"

🎯 Your Task:
Write a Python program using conditional expressions to give the appropriate advice based on the input number of steps.

enhance it even further by referencing ideas from:

data analysis projects

user experience improvements

automation, persistence, and visualization

"""

import json
import datetime
import matplotlib.pyplot as plt
import os

# 🚀 Welcome Message
print("🏃 Welcome to Smart Fitness Tracker\n")

# 📥 Input Today's Steps
try:
    steps = int(input("Enter the number of steps you walked today: "))
    if steps < 0:
        raise ValueError("Step count cannot be negative.")
except ValueError as e:
    print(f"❌ Invalid input: {e}")
    exit()

# 📅 Get today's date as a label
today = datetime.date.today().isoformat()

# 📂 Load previous data if available
log_file = 'fitness_log.json'
fitness_log = {}

if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        fitness_log = json.load(f)
        print("📁 Loaded your previous step data.")
else:
    print("📂 Starting a new fitness log.")

# 🧠 Advice Based on Steps
advice = (
    "Too little movement. Try a short walk!" if steps < 1000 else
    "Good start! Try to move more today." if steps < 5000 else
    "Nice job! You're staying active." if steps < 10000 else
    "Excellent! You've reached your goal!"
)

# ✅ Save today's data
fitness_log[today] = {"steps": steps, "advice": advice}

with open(log_file, 'w') as f:
    json.dump(fitness_log, f, indent=2)
print(f"\n📝 Logged {steps} steps for {today}.")

# 💬 Print personalized advice
print(f"\n🧠 Advice: {advice}")

# 📈 Visualization of Step Trends
dates = list(fitness_log.keys())
step_values = [fitness_log[d]["steps"] for d in dates]

plt.figure(figsize=(8, 4))
plt.plot(dates, step_values, marker='o', linestyle='-', linewidth=2)
plt.title("📊 Step Count Trend")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# 🧹 Optional: Clear Data
if input("\nDo you want to clear your step history? (yes/no): ").strip().lower() == "yes":
    os.remove(log_file)
    print("🧼 Fitness log cleared.")
else:
    print("📌 Keeping your step history.")
