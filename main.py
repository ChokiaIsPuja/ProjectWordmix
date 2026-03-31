import random
from spellchecker import SpellChecker

#bahasa
spell = SpellChecker(language='en')


#array word yang memiliki panjang 5 karakter dari kamus spellchecker
WORD_LIST = [w for w in spell.word_frequency.keys() if len(w) == 5]

while True:  # Main game loop for restarting
    TARGET = random.choice(WORD_LIST)
    MAX_TRIES = 6 #jumlah percobaan

    print("Wordle-like game: guess the 5-letter word (type 'quit' to exit)")

    while MAX_TRIES > 0:
        guess = input(f"{MAX_TRIES} tries left. Enter guess: ").strip().lower()
        if guess == "quit":
            print("Quit. Bye!")
            exit()  # Exit the entire program
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly 5 alphabetic characters.")
            continue
        if guess not in WORD_LIST:
            print("Word not in allowed 5-letter dictionary.")
            continue

        # letter grading
        feedback = []
        target_chars = list(TARGET)

        # green pass
        for i, ch in enumerate(guess):
            if TARGET[i] == ch:
                feedback.append("🟩")
                target_chars[i] = None
            else:
                feedback.append(None)

        # yellow/gray pass
        for i, ch in enumerate(guess):
            if feedback[i] is None:
                if ch in target_chars:
                    feedback[i] = "🟨"
                    target_chars[target_chars.index(ch)] = None
                else:
                    feedback[i] = "⬛"

        print(f"{guess} -> {''.join(feedback)}")

        if guess == TARGET:
            print("🎉 Correct! You win!")
            break

        MAX_TRIES -= 1

    if MAX_TRIES == 0:
        print(f"Game over. The word was: {TARGET}")

    # Ask to play again
    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
