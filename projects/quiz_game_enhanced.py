'''
How can I create an interactive multiple-choice computer quiz in Python that uses a question bank, 
tracks score, gives real-time feedback, randomizes questions, and allows replaying? Use the learnings
from chapter 1 and enhance the quiz game.
'''

import random
import pyttsx3
import pyjokes
from PIL import Image, ImageDraw, ImageFont

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def generate_result_image(score, total):
    img = Image.new('RGB', (400, 200), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    message = f"You scored {score} out of {total}!"
    d.text((20, 80), message, font=font, fill=(255, 255, 0))
    img_path = "quiz_result.png"
    img.save(img_path)
    speak(f"Your result image has been saved as {img_path}.")

def run_quiz():
    speak("Welcome to the Enhanced Computer Quiz!")
    playing = input("Do you want to play? (yes/no): ").strip().lower()
    if playing != "yes":
        speak("Maybe next time!")
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
        speak("\n" + q["question"])
        for option in q["options"]:
            speak(option)
        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()

        if user_answer == q["answer"]:
            speak("✅ Correct!")
            score += 1
        else:
            correct_option = q['options'][ord(q['answer']) - 97]
            speak(f"❌ Incorrect! The correct answer was: {correct_option}")

    percentage = (score / len(questions)) * 100
    speak(f"Quiz Completed! You got {score} out of {len(questions)} correct.")
    speak(f"Your Score: {percentage:.2f}%")

    # Generate result image
    generate_result_image(score, len(questions))

    # Show a joke
    joke = pyjokes.get_joke()
    speak("Here’s a joke to cheer you up!")
    speak(joke)

    retry = input("Would you like to try again? (yes/no): ").strip().lower()
    if retry == "yes":
        run_quiz()
    else:
        speak("Thanks for playing! Goodbye!")

run_quiz()
