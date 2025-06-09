'''
"Time Travel Age Swapper"
🔍 Concept:
This is a quirky, creative terminal-based project where:

You enter your name and age.

It swaps your age with a character from a random time era (like a Roman gladiator, a 2300 AI bot, or a 90s disco dancer).

It shows type usage, typecasting, rules of naming, and operators.

Uses fun math and storytelling logic with just these fundamentals.


'''

import random

# ==== Characters List (name, year they live in) ====
characters = [
    ("Cleopatra", -50),  # 50 BC
    ("Shakespeare", 1600),
    ("Disco Dancer", 1978),
    ("AI Bot X", 2300),
    ("Caveman Zog", -10000),
    ("Medieval Knight", 1200)
]

# ==== Get user input ====
user_name = input("What's your name? ")
user_age = input("What's your age? ")

# ==== Type check and cast ====
print("You entered age as:", user_age, "| Type:", type(user_age))
user_age = int(user_age)  # typecasting string to int

# ==== Pick a random character ====
character, character_year = random.choice(characters)
current_year = 2025

# ==== Calculate their age ====
character_age = current_year - character_year
age_difference = abs(character_year - current_year)

# ==== Swap Logic ====
if character_year > current_year:
    user_swapped_age = user_age + age_difference  # Future swap
    character_swapped_age = character_age - age_difference
else:
    user_swapped_age = user_age - age_difference  # Past swap
    character_swapped_age = character_age + age_difference

# ==== Final output ====
print("\n🎭 TIME TRAVEL AGE SWAPPER 🔄")
print(f"{user_name}, you've swapped timelines with {character} from year {character_year}!")

print(f"\n🕒 You are now {user_swapped_age} years old in the year {character_year}.")
print(f"🤖 {character} is now {character_swapped_age} years old in 2025!")

# ==== Show types again ====
print(f"\nDebug: Your age type is now: {type(user_swapped_age)}")
