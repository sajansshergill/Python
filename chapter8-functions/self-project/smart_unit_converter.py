"""
Project Objective
Build a mini utility program that acts as a multi-tool:

Converts units (temperature, length)

Prints dynamic star patterns

Removes words from strings

Recursively computes math operations like sum or factorial

Prints custom multiplication tables

All of these will be implemented using functions, and you’ll optionally build a menu-driven CLI interface.

"""

# Smart Utility Toolkit – Functions, Recursion, and Patterns

def find_greatest_of_three(a, b, c):
    return max(a, b, c)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def inches_to_cms(inches):
    return inches * 2.54

def sum_natural_numbers(n):
    if n == 1:
        return 1
    return n + sum_natural_numbers(n - 1)

def print_star_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

def remove_and_strip(text, word):
    return text.replace(word, "").strip()

def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def custom_print(value, end_char):
    print(value, end=end_char)

# ------------------- MAIN MENU -------------------

def show_menu():
    print("\n🛠️ Smart Utility Toolkit")
    print("1. Find greatest of three numbers")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Convert Inches to Centimeters")
    print("4. Sum of First N Natural Numbers (Recursive)")
    print("5. Print Star Pattern")
    print("6. Remove and Strip Word from Text")
    print("7. Print Multiplication Table")
    print("8. Custom Print without Newline")
    print("9. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
        print(f"The greatest number is: {find_greatest_of_three(a, b, c)}")

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius)} °F")

    elif choice == "3":
        inches = float(input("Enter length in inches: "))
        print(f"Length in centimeters: {inches_to_cms(inches)} cm")

    elif choice == "4":
        n = int(input("Enter value of n: "))
        print(f"Sum of first {n} natural numbers is: {sum_natural_numbers(n)}")

    elif choice == "5":
        n = int(input("Enter number of lines for star pattern: "))
        print_star_pattern(n)

    elif choice == "6":
        text = input("Enter a sentence: ")
        word = input("Enter the word to remove: ")
        result = remove_and_strip(text, word)
        print(f"Result after removal: '{result}'")

    elif choice == "7":
        num = int(input("Enter a number to print its multiplication table: "))
        print_table(num)

    elif choice == "8":
        value = input("Enter text to print without newline: ")
        custom_print(value, end_char="")  # This ends the print without newline

    elif choice == "9":
        print("👋 Exiting Smart Utility Toolkit. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 9.")
