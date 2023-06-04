"""
Python basics, Problem Set, hangman.py
Name: Thang Nguyen
Collaborators: 
Time spent: 
"""

# ---------------------------------------------------------------------------- #
#                                 Hangman Game                                 #
# ---------------------------------------------------------------------------- #


# -------------------------------- Helper code ------------------------------- #
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME, "r") as inFile:
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# ---------------------------- end of helper code ---------------------------- #


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far, assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    # convert all letters in letter_guessed to lowercase
    letters_guessed_in_lowercase = [c.lower() for c in letters_guessed]
    # check if characters in secret word are in letter guessed
    if all(c in letters_guessed_in_lowercase for c in secret_word):
        return True    


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for c in secret_word:
        # append character if  it's in letter_guessed
        if c in letters_guessed:
            guessed_word += c
        # append underscore(_) if  character is not in letter_guessed
        else:
            guessed_word += "_"
    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = string.ascii_lowercase
    for c in letters_guessed:
        # remove character in available if it appears in letter_guessed
        available_letters = available_letters.replace(c, "")
    return available_letters


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")

    # Game loops if condition is sastisfied      
    while (guesses_remaining > 0):
        print("-------------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guessed_letter = input("Please guess a letter: ").lower()
        
        # Input can only be alpha, if not print warning
        if (guessed_letter.isalpha() == False):
            warnings_remaining -= 1
            if (warnings_remaining < 0):
                guesses_remaining -= 1
                continue
            else:
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
                continue

        # Can not guess guessed letters, print warning
        if (guessed_letter in letters_guessed):
            warnings_remaining -= 1
            if (warnings_remaining < 0):
                guesses_remaining -= 1
                continue
            else:
                print(f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings: {get_guessed_word(secret_word, letters_guessed)}")
                continue


        letters_guessed.append(guessed_letter)

        # Player wins if guesses correctly all letters in secret word
        if (is_word_guessed(secret_word, letters_guessed)):
            total_score = guesses_remaining * len(set(secret_word))
            print("-------------")
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break
        else:
            if (guessed_letter in secret_word):
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                continue
            else:
                if (guessed_letter in "aeiou"):
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    guesses_remaining -= 2
                    continue
                else:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    guesses_remaining -= 1
                    continue

        

    # Player loses by running out of guesses
    if (guesses_remaining <= 0):
        print("-------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# ---------------------------------------------------------------------------- #


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    my_word = my_word.replace(" ", "")
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == "_":
                count +=1
                continue
            elif my_word[i] == other_word[i]:
                count +=1
            else:
                return False
    else:
        return False
    if count == len(my_word):
        return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word

    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    suggested_word = 0
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            suggested_word += 1
            print(word, end=" ")
    print("\n")
    if suggested_word == 0:
        print("No matches found")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # TODO: FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")

    # Game loops if condition is sastisfied      
    while (guesses_remaining > 0):
        print("-------------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guessed_letter = input("Please guess a letter: ").lower()

        # Show suggested words
        if (guessed_letter == "*"):
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        
        # Input can only be alpha, print warning, warning remaning lose 1 point
        if (guessed_letter.isalpha() == False):
            warnings_remaining -= 1
            if (warnings_remaining < 0):
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                continue
            else:
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
                continue

        # Can not guess guessed word, print warning, warning remaning lose 1 point
        if (guessed_letter in letters_guessed):
            warnings_remaining -= 1
            if (warnings_remaining < 0):
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                continue
            else:
                print(f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings: {get_guessed_word(secret_word, letters_guessed)}")
                continue

        letters_guessed.append(guessed_letter)

        # Player wins if guesses correctly all letters in secret word
        if (is_word_guessed(secret_word, letters_guessed)):
            total_score = guesses_remaining * len(set(secret_word))
            print("-------------")
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break
        else:
            if (guessed_letter in secret_word):
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                continue
            else:
                # player loses 2 guesses if guess a vowel wrong
                if (guessed_letter in "aeiou"):
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    guesses_remaining -= 2
                    continue
                else:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    guesses_remaining -= 1
                    continue

    # Player loses by running out of guesses
    if (guesses_remaining <= 0):
        print("-------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word="anple")

# ---------------------------------------------------------------------------- #

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
