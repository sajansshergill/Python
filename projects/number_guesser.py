"""
Guess the Number!
Type the highest number you'd like to guess up to, and the computer will choose a secret number 
between 1 and that number.
You'll keep guessing until you get it right — and it will tell you if you're too high or too low.
It will also count how many guesses you took!
Ready to play?

"""

import random
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    speak("Welcome to the Number Guessing Game!")

    while True:
        top_of_range = input("\n🔢 Type the highest number for the range (must be > 0): ")

        if top_of_range.isdigit():
            top_of_range = int(top_of_range)
            if top_of_range > 0:
                break
            else:
                print("⚠️ Please enter a number greater than 0.")
                speak("Please enter a number greater than 0.")
        else:
            print("⚠️ That’s not a valid number.")
            speak("That’s not a valid number.")

    random_number = random.randint(1, top_of_range)
    guesses = 0

    while True:
        user_guess = input(f"🤔 Make a guess between 1 and {top_of_range}: ")
        guesses += 1

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("⚠️ Please type a valid number.")
            speak("Please type a valid number.")
            continue

        if user_guess == random_number:
            result = f"You got it in {guesses} guesses!"
            print("🎉 " + result)
            speak(result)
            break
        elif user_guess > random_number:
            print("📉 Too high!")
            speak("Too high!")
        else:
            print("📈 Too low!")
            speak("Too low!")

    play_again = input("🔁 Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("👋 Thanks for playing!")
        speak("Thanks for playing!")

# Start the game
play_game()
