"""secret"""
def is_word_guessed(secret_word, letters_guessed):
    """guess"""
    cou = 0
    for i in range(len(secret_word))
        for k in range(len(letters_guessed))
            if secret_word[i] == letters_guessed[j]:
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
