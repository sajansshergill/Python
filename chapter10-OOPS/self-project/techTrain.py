"""
TechTrain – A Multi-Service Python App with Programmers, Calculator, and Ticket Booking
"""

"""
    🎯 Project Objective
Create a multi-functional command-line system for:

Storing employee (Programmer) details for Microsoft

Doing quick developer math (Calculator)

Simulating a Train booking system

Understanding class vs object scope, and self renaming

🔧 Modules in the Project
🧩 1. Programmer Class
Stores name, language, and company (Microsoft)

Methods:

__init__() to initialize

get_info() to return details

🧩 2. Calculator Class
Performs square, cube, square root calculations.

Methods:

square(n), cube(n), sqrt(n)

@staticmethod greet() → returns “Hello, Developer!”

🧩 3. Class Attribute vs Object Attribute Demo
Class with a = 10

Then update it via obj.a = 0 and show it doesn’t change the class attribute.

🧩 4. Train Class
Simulates Indian Railways:

Attributes:

name, seats, fare

Methods:

book_ticket() → reduces seat count

get_status() → shows remaining seats

get_fare() → returns fare

🧪 5. self Renaming Demo
Create a class using harry instead of self for all methods — to show it's just a naming convention.
    """
    
import math

# -------------------- 1. Programmer Class --------------------
class Programmer:
    company = "Microsoft"

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def get_info(self):
        return f"{self.name} works at {self.company} and programs in {self.language}."


# -------------------- 2. Calculator Class --------------------
class Calculator:
    def square(self, n):
        return n ** 2

    def cube(self, n):
        return n ** 3

    def sqrt(self, n):
        return round(math.sqrt(n), 2)

    @staticmethod
    def greet():
        return "Hello, Developer!"


# -------------------- 3. Class vs Object Attribute Demo --------------------
class DemoClass:
    a = 10  # Class attribute


# -------------------- 4. Train Class --------------------
class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"✅ Ticket booked! Seats left: {self.seats}")
        else:
            print("❌ Sorry, train is full!")

    def get_status(self):
        print(f"🚆 Train '{self.name}' has {self.seats} seat(s) left.")

    def get_fare(self):
        print(f"🎟️ Fare for '{self.name}': ₹{self.fare}")


# -------------------- 5. self Parameter Renamed Demo --------------------
class RenameSelfDemo:
    def __init__(harry, val):
        harry.value = val

    def show(harry):
        print(f"Value stored is: {harry.value}")


# -------------------- MAIN MENU --------------------
def show_menu():
    print("\n📦 TechTrain Multi-Service App")
    print("1. Add Programmer Info")
    print("2. Use Calculator")
    print("3. Demonstrate Class vs Object Attribute")
    print("4. Train Ticket Booking")
    print("5. Show 'self' Renaming Example")
    print("6. Exit")

# -------------------- MAIN PROGRAM --------------------
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter programmer's name: ")
        lang = input("Enter programming language: ")
        dev = Programmer(name, lang)
        print(dev.get_info())

    elif choice == "2":
        calc = Calculator()
        print(Calculator.greet())
        n = float(input("Enter a number: "))
        print(f"Square of {n}: {calc.square(n)}")
        print(f"Cube of {n}: {calc.cube(n)}")
        print(f"Square root of {n}: {calc.sqrt(n)}")

    elif choice == "3":
        obj = DemoClass()
        print(f"Before: Class attribute DemoClass.a = {DemoClass.a}")
        obj.a = 0  # Changes only for object
        print(f"After: Object attribute obj.a = {obj.a}")
        print(f"Still: Class attribute DemoClass.a = {DemoClass.a}")

    elif choice == "4":
        train = Train("Shatabdi Express", 5, 150)
        while True:
            print("\nTrain Menu: 1.Book  2.Status  3.Fare  4.Back")
            t_choice = input("Choose: ")
            if t_choice == "1":
                train.book_ticket()
            elif t_choice == "2":
                train.get_status()
            elif t_choice == "3":
                train.get_fare()
            elif t_choice == "4":
                break
            else:
                print("❌ Invalid choice.")

    elif choice == "5":
        obj = RenameSelfDemo(42)
        obj.show()

    elif choice == "6":
        print("👋 Exiting TechTrain App. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select 1–6.")
