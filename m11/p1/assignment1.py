"""word"""
def get_word_score(word, n1_):
    """wordscore"""
    dict1_ = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
              'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 
              'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    length = len(word)
    sum1 = 0
    if length <= n1_:
        for j in word:
            if j in dict1_.keys():
                sum1 = sum1 + dict1_[j]
        sum1 = sum1 * length
        if length == n1_:
            sum1 = sum1 + 50
        return sum1
    return "invalid"
def main():
    """score"""
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))
if __name__ == "__main__":
    main()
