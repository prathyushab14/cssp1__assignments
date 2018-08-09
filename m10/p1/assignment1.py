"""string"""
def get_available_letters(letters_guessed):
    """dictionaries"""
    import string
    s = ''
    key1 = list(string.ascii_lowercase)
    val1 = key1
    dic1 = dict(zip(key1,val1))
    for i in letters_guessed:
        if i in dic1.key1():
            del dic1[i]
    for j in dic1.key1():
        s = s + dic[i]
    return s
def main():
    """string"""
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
