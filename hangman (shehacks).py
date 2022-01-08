try:
    word = input("Enter a word: ")
    turns = int(input("Enter number of guesses: "))
    guesses = ""

    while turns > 0:
        failed = 0
        print('WORD:',end="")
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        print("\nGUESSES LEFT: ", turns)
        if failed == 0:
            print("\nCorrect.")

            break

        print()

        guess = input("Guess a character: ")
        guesses += guess
        turns -=1

        if guess not in word:
            print("Incorrect. Letter is not in the word")


            if turns == 0:
                print("No guesses left :(")
except Exception as e:
    print(e)
