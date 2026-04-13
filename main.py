import random
from spellchecker import SpellChecker

# initialize spellchecker
spell = SpellChecker(language='en')

# 5-letter word list
WORD_LIST = [w for w in spell.word_frequency.keys() if len(w) == 5]

while True:
    TARGET = random.choice(WORD_LIST)
    MAX_TRIES = 5

    # STACK (list in python)
    stack = []

    print("Wordle-like game with STACK system")
    print("Commands: 'undo' to remove last guess, 'quit' to exit")

    while MAX_TRIES > 0:
        guess = input(f"{MAX_TRIES} tries left. Enter guess: ").strip().lower()

        if guess == "quit":
            print("Quit. Bye!")
            exit()

        # POP (undo)
        if guess == "undo":
            if stack:
                removed = stack.pop()
                MAX_TRIES += 1
                print(f"Removed last guess: {removed}")
            else:
                print("Stack empty, nothing to undo.")
            continue

        # validation
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly 5 alphabetic characters.")
            continue

        if guess not in WORD_LIST:
            print("Word not in allowed 5-letter dictionary.")
            continue

        # PUSH
        stack.append(guess)

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

        # PEEK
        print("Last guess (PEEK):", stack[-1])

        # DISPLAY
        print("All guesses (STACK):", stack)

        if guess == TARGET:
            print("🎉 Correct! You win!")
            break

        MAX_TRIES -= 1

    if MAX_TRIES == 0:
        print(f"Game over. The word was: {TARGET}")

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
