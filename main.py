import time
import random
import textwrap

# Sample sentences (you can expand this)
sentences = [
    "Python is an awesome programming language.",
    "Typing fast is a useful skill.",
    "Practice makes perfect.",
    "Debugging is twice as hard as writing the code in the first place."
]

def typing_test():
    print("💥 Welcome to the Typing Speed Test!\n")
    input("Press Enter when you're ready...")

    target = random.choice(sentences)
    print("\nType this:\n")
    print(textwrap.fill(target, width=50))
    
    start = time.time()
    typed = input("\nStart typing:\n")
    end = time.time()
    
    time_taken = end - start
    wpm = len(typed.split()) / (time_taken / 60)
    
    correct_chars = sum(1 for a, b in zip(typed, target) if a == b)
    accuracy = (correct_chars / len(target)) * 100

    print(f"\n⏱ Time Taken: {round(time_taken, 2)} seconds")
    print(f"🚀 WPM: {round(wpm, 2)}")
    print(f"🎯 Accuracy: {round(accuracy, 2)}%")

typing_test()
