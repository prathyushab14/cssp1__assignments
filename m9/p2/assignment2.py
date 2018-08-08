'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
'''
def get_guessed_word(secret_word, letters_guessed):
    l_1 = len(secret_word)
    l_2 = len(letters_guessed)
    a_str = " "
    for i in range(l_1):
        cou = 0
        for k in range(l_2):
            if secret_word[i] == letters_guessed[k]
                a_str = a_str + secret_word[i]
                cou += 1
        if cou == 0
            a_str = a_str + '_'
def main():
    """secret"""
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))
if __name__ == "__main__":
    main()
