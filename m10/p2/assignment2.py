'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''
def get_available_letters(letters_guessed):
    """dictionaries"""
    import string
    s1_ = ''
    key1 = list(string.ascii_lowercase)
    val1 = key1
    dic1 = dict(zip(key1, val1))
    for i in letters_guessed:
        if i in dic1.values():
            del dic1[i]
    for j in dic1.values():
        s1_ = s1_ + dic1[j]
    return s1_
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
def is_word_guessed(secret_word, letters_guessed):
    
    secret_set = set(secret_word)
    intersect = secret_set.intersection(set(letters_guessed))
    return bool(len(intersect) == len(secret_set))

def get_guessed_word(secret_word, letters_guessed):
    """guess"""
    l_1 = len(secret_word)
    l_2 = len(letters_guessed)
    a_str = ""
    for i in range(l_1):
        cou = 0
        for k in range(l_2):
            if secret_word[i] == letters_guessed[k]:
                cou += 1
                if cou == 1:
                    a_str = a_str + secret_word[i]
                break
        if cou == 0:
            a_str = a_str + ' _ '
    return a_str
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("the guessed word has",len(secretWord), "letters")
    print("Guess a letter")
    guess = 10
    letters_guessed = ""
    while guess>0 and (not is_word_guessed(secretWord, letters_guessed)):
        inp_t = input("enter the guess")
        
        if inp_t in letters_guessed:
            letters_guessed += inp_t
            print("you have already guessed this letter",get_guessed_word(secretWord, letters_guessed))
            print("No of guesses left:",guess)
        elif inp_t in secretWord:
            letters_guessed += inp_t
            print("Good Guess:",get_guessed_word(secretWord, letters_guessed))
            print("No of guesses left:",guess)
        else:
            letters_guessed += inp_t
            print("Oops! Made a wrong guess", get_guessed_word(secretWord, letters_guessed))
            guess -= 1
            print("No of guesses left:",guess)
    if is_word_guessed(secretWord,letters_guessed):
            print("You Won!")
    else:
            print("lost",secretWord)







def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    #secretWord = chooseWord(wordlist).lower()
    secretWord = "nani"
    hangman(secretWord)


if __name__ == "__main__":
    main()
