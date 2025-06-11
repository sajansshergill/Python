# Mini Voting System for Favorite Programming Languages

"""
💡 Project Features
1. Register votes
Ask 4 users (or more) to enter their name and favorite programming language.

Use a dictionary to store:
{ "Alice": "Python", "Bob": "JavaScript", ... }

2. Handle Duplicate Keys
If a name already exists in the dictionary, notify the user that their vote has been updated.

3. Display all unique languages voted for
Use a set to store only unique language names.

4. Compare popularity
Accept two different language names from user and check:

Whether both were voted for (using intersection)

Whether one is a subset/superset of another (bonus use of issubset/issuperset)

5. Copy and Reset Function
Let the user copy() the dictionary or clear() it after voting ends.
"""

# Mini Voting System – Using Dictionaries and Sets (Final Version)

print("🗳️ Welcome to the Mini Voting System!\n")

# Step 1: Initialize empty dictionary and set
votes = {}
unique_languages = set()

# Step 2: Allow multiple users to vote
num_users = 4
for i in range(1, num_users + 1):
    name = input(f"Enter name of voter {i}: ").strip()

    language = input(f"Hi {name}, what's your favorite programming language? ").strip().title()

    # Check for duplicate name (will overwrite)
    if name in votes:
        print(f"⚠️ Note: Overwriting previous vote for {name}.\n")

    votes.update({name: language})
    unique_languages.add(language)

print("\n📊 Voting Complete!")
print("-" * 30)

# Step 3: Display all votes
print("📋 All Votes (Name → Language):")
for name, lang in votes.items():
    print(f"{name} → {lang}")

# Step 4: Show unique languages voted for
print(f"\n🧠 Unique programming languages voted for: {unique_languages}")
print(f"Total unique languages: {len(unique_languages)}")

# Step 5: Compare two languages
print("\n🔍 Let's compare if two languages were voted for.")
lang1 = input("Enter first language to check: ").strip().title()
lang2 = input("Enter second language to check: ").strip().title()

lang_check_set = {lang1, lang2}
intersection = unique_languages.intersection(lang_check_set)

if intersection:
    print(f"✅ Found these voted languages: {intersection}")
else:
    print("❌ None of the entered languages were voted.")

# Step 6: Demonstrate .copy() and .clear()
votes_backup = votes.copy()
print("\n📦 Backup of votes dictionary created.")

clear_choice = input("Do you want to clear all votes? (yes/no): ").strip().lower()
if clear_choice == "yes":
    votes.clear()
    unique_languages.clear()
    print("🧹 All votes and languages have been cleared.")
else:
    print("✅ Keeping current data.")

# Step 7: Final Output
print("\n📁 Final state of vote dictionary:")
print(votes)

print("\n🗃️ Backup copy remains safe:")
print(votes_backup)
