"""
Safe Table Toolkit – Smart Multiplication & File Handler
🎯 Project Objective
Create a menu-driven Python app that:

Opens multiple files, reporting missing ones without crashing

Prints specific indexed elements from a list using enumerate()

Generates a multiplication table using list comprehension

Handles ZeroDivisionError and safely computes division

Stores the generated table into a file called Tables.txt

✅ Features You’ll Implement:
| Question | What the feature will do                                                        |
| -------- | ------------------------------------------------------------------------------- |
| Q1       | Open 1.txt, 2.txt, 3.txt with graceful error messages if any are missing        |
| Q2       | Print 3rd, 5th, and 7th elements from a sample list using `enumerate()`         |
| Q3 & Q5  | Generate multiplication table using list comprehension and save to `Tables.txt` |
| Q4       | Ask user for `a` and `b`, then safely print `a/b` or "infinite" if `b = 0`      |

"""

from pathlib import Path

def open_three_files():
    print("🔍 Opening 1.txt, 2.txt, 3.txt...")
    for i in range(1, 4):
        file_path = Path(f"{i}.txt")
        if file_path.exists():
            print(f"✅ {file_path.name} opened successfully.")
            content = file_path.read_text(encoding="utf-8")
            print(f"📄 {file_path.name} content:\n{content}")
        else:
            print(f"⚠️ {file_path.name} is missing. Skipping...")

def print_selected_elements():
    sample_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
    print("🔢 Extracting 3rd, 5th, and 7th elements from sample list:")
    for index, value in enumerate(sample_list):
        if index in [2, 4, 6]:
            print(f"Index {index + 1} → {value}")

def generate_table():
    try:
        num = int(input("Enter a number for its multiplication table: "))
        table = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
        print("\n📋 Multiplication Table:")
        for line in table:
            print(line)

        # Save to file
        Path("Tables.txt").write_text("\n".join(table), encoding="utf-8")
        print("\n✅ Table saved to Tables.txt")

    except ValueError:
        print("❌ Please enter a valid number.")

def safe_division():
    try:
        a = int(input("Enter numerator (a): "))
        b = int(input("Enter denominator (b): "))
        result = a / b
        print(f"🧮 Result: {result}")
    except ZeroDivisionError:
        print("⚠️ Cannot divide by zero. Result is: Infinite.")
    except ValueError:
        print("❌ Invalid input. Please enter integers only.")

# ------------------ CLI MENU ------------------
def show_menu():
    print("\n========= Safe Table Toolkit =========")
    print("1. Open 1.txt, 2.txt, and 3.txt")
    print("2. Print 3rd, 5th, and 7th elements using enumerate()")
    print("3. Generate and store multiplication table")
    print("4. Perform safe division a / b")
    print("5. Exit")
    print("=======================================")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            open_three_files()
        elif choice == "2":
            print_selected_elements()
        elif choice == "3":
            generate_table()
        elif choice == "4":
            safe_division()
        elif choice == "5":
            print("👋 Exiting Safe Table Toolkit. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    main()
