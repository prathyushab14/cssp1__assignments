"""assignment2"""
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
    """words"""
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    return random.choice(wordlist)
wordlist = loadWords()
def hangman(secretWord):
    """hangman"""
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
    """secret"""
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
if __name__ == "__main__":
    main()
