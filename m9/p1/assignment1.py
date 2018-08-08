"""secret"""
def is_word_guessed(secret_word, letters_guessed):
    """guess"""
    cou = 0
    l1 = len(secret_word)
    l2 = len(letters_guessed)
    for i in range(l1):
        for k in range(l2):
            if secret_word[i] == letters_guessed[k]:
                cou += 1
    return bool(cou == len(secret_word))
def main():
    """guess"""
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
    print(is_word_guessed(secret_word, list1))
if __name__ == "__main__":
    main()
