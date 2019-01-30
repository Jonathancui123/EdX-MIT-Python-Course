# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    solved = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            solved = False
            break
    return solved

#print(isWordGuessed("bigapple", ['a','p','l','e','g','i','b']))



def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far."""
    progress = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            progress += letter
        else:
            progress += "_ "
    return progress


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    available = ""
    for letter in alphabet:
        if letter not in lettersGuessed:
            available += (letter.upper() + " ")
    return available

#print(getAvailableLetters(['a','e', 'i', 'k', 'p', 'r', 's','l']))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    '''
    print("_____________________________________________")
    print("Welcome to Hangman! Try and guess the secret word!")
    print("The secret word has", len(secretWord), "letters.")
    print("_____________________________________________")
    print("""Before you begin... Be warned.
        After 9 incorrect guesses...
                      The man will be...
                                         HANGED!""")
    loseCondition = 9
    lettersGuessed = []
    wrongGuesses = 0
    roundCounter = 0
    def startround (secretWord, wrongGuesses, roundCounter):
        if roundCounter > 1:
            print("So far: "+ getGuessedWord(secretWord, lettersGuessed))
            print("Letters to guess are:", getAvailableLetters(lettersGuessed))
        guess = input("Enter a letter and press enter!: ").lower()
        print("_____________________________________________")
        if len(guess) > 1 or guess not in "abcdefghijklmnopqrstuvwxyz" or len(guess) == 0:
            print("Expecting a single letter as the input :/ ")
        elif guess in lettersGuessed:
            print("You've already guessed that letter! Guess again.")
        elif guess in secretWord and guess != '':
            print("Good guess!")
            lettersGuessed.append(guess)
        else:
            lettersGuessed.append(guess)
            wrongGuesses += 1
            guessesLeft = loseCondition - wrongGuesses
            if wrongGuesses <= loseCondition:
                print("You have", guessesLeft, "wrong guesses remaining!")
        return  wrongGuesses






    while isWordGuessed(secretWord, lettersGuessed) == False and wrongGuesses < loseCondition:
        roundCounter += 1
        wrongGuesses = startround(secretWord,wrongGuesses,roundCounter)

    if wrongGuesses >= loseCondition:
        print("""___________
|         |
|         0
|        /|/
|        | |
|
|""")
        print("The word was:", secretWord)
        print("GAME OVER. Play again!")
    else:
        print("The secret word was:", secretWord)
        print("Good game!! You win!!!!")


    '''* Ask the user to supply one guess (i.e. letter) per round.'''


    '''* The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.'''

    '''* After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.'''

hangman(chooseWord(loadWords()))




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
