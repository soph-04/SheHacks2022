word = input("Enter a word: ")
turns = int(input("Enter number of guesses: "))
guesses = ""

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("Correct.")

        break

    print()

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Incorrect. Letter is not in the word")

        print("GUESSES LEFT: ", turns)

        if turns == 0:
            print("No guesses left :(")
