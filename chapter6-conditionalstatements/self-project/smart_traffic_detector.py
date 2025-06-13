"""
Smart Traffic Signal Detector:-
You're designing logic for a smart traffic signal system that changes light status based on these conditions:

Input from the user:
is_ambulance_coming → "yes" or "no"

current_traffic_density → "high", "medium", or "low"

time_of_day → "peak" or "off-peak"

Logic rules:
If an ambulance is coming, the signal should turn green immediately.

If traffic density is high during peak hours, set the signal to stay green longer.

If traffic density is low during off-peak hours, set the signal to switch quickly (short green).

In all other cases, set the signal to normal timing.

Track traffic snapshots using a dictionary with time labels (e.g., "9AM", "5PM").

Analyze ambulance cases (how many times it occurred).

Get popular traffic patterns (how often a certain density shows up).

Compare two time windows (are both peak? any ambulance?).

Use .copy() and .clear() to manage logs.



"""

# 🚦 Smart Traffic Signal Manager – Inspired by Voting System

print("🚦 Welcome to Smart Traffic Signal Manager\n")

traffic_log = {}
unique_densities = set()

num_entries = int(input("How many time-based entries do you want to log? "))

for i in range(num_entries):
    time_label = input(f"\nEnter time label (e.g., 8AM, 5PM) for entry {i+1}: ").strip().upper()
    is_ambulance = input("Is an ambulance coming? (yes/no): ").strip().lower()
    density = input("Traffic density (high/medium/low): ").strip().lower()
    time_type = input("Time of day (peak/off-peak): ").strip().lower()

    traffic_log[time_label] = {
        "ambulance": is_ambulance,
        "density": density,
        "time_type": time_type
    }
    unique_densities.add(density)

print("\n📊 Traffic Log Summary")
print("-" * 30)
for time, info in traffic_log.items():
    print(f"{time} → {info}")

print(f"\n🧠 Unique traffic densities: {unique_densities}")
print(f"🚑 Number of times ambulance came: {sum(1 for v in traffic_log.values() if v['ambulance'] == 'yes')}")

# 🔍 Compare Two Time Labels
print("\n🔍 Compare traffic between two time periods.")
t1 = input("Enter first time label: ").strip().upper()
t2 = input("Enter second time label: ").strip().upper()

if t1 in traffic_log and t2 in traffic_log:
    a1, a2 = traffic_log[t1]['ambulance'], traffic_log[t2]['ambulance']
    d1, d2 = traffic_log[t1]['density'], traffic_log[t2]['density']

    print(f"\n🕒 {t1} ambulance: {a1}, density: {d1}")
    print(f"🕒 {t2} ambulance: {a2}, density: {d2}")

    if a1 == "yes" and a2 == "yes":
        print("✅ Both had ambulances.")
    elif d1 == d2:
        print("⚖️ Both had same traffic density.")
    else:
        print("📉 Traffic conditions varied.")
else:
    print("❌ One or both time labels not found.")

# 📦 Backup and Clear Option
log_backup = traffic_log.copy()
if input("\nDo you want to clear the traffic log? (yes/no): ").strip().lower() == "yes":
    traffic_log.clear()
    unique_densities.clear()
    print("🧹 Traffic log cleared.")
else:
    print("🗂️ Keeping current traffic data.")

print("\n📁 Final Traffic Log:")
print(traffic_log)

print("\n🗃️ Backup Log:")
print(log_backup)
