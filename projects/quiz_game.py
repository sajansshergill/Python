'''
How can I create an interactive multiple-choice computer quiz in Python that uses a question bank, 
tracks score, gives real-time feedback, randomizes questions, and allows replaying?
'''

import random

def run_quiz():
    print("Welcome to the Enhanced Computer Quiz!")
    playing = input("Do you want to play? (yes/no): ").strip().lower()
    if playing != "yes":
        print("Maybe next time!")
        return

    questions = [
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Core Processing Unit", "D. Central Print Unit"],
            "answer": "a"
        },
        {
            "question": "What does GPU stand for?",
            "options": ["A. General Processing Unit", "B. Graphics Processing Unit", "C. Graphical Power Unit", "D. Graphic Processing Utility"],
            "answer": "b"
        },
        {
            "question": "What is the purpose of RAM in a computer?",
            "options": ["A. Store permanent files", "B. Process graphics", "C. Temporarily store data for quick access", "D. Power the system"],
            "answer": "c"
        },
        {
            "question": "Which of these is an example of non-volatile memory?",
            "options": ["A. RAM", "B. ROM", "C. CPU Cache", "D. Registers"],
            "answer": "b"
        },
        {
            "question": "How many layers are in the OSI Model?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "c"
        }
    ]

    score = 0
    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {q['options'][ord(q['answer']) - 97]}")

    print(f"\nQuiz Completed! You got {score}/{len(questions)} correct.")
    print(f"Your Score: {(score / len(questions)) * 100:.2f}%")

    retry = input("Would you like to try again? (yes/no): ").strip().lower()
    if retry == "yes":
        run_quiz()
    else:
        print("Thanks for playing!")

run_quiz()
