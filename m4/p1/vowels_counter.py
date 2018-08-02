""" vowels count"""
#Assume s is a string of lower case characters.
#Number of vowels: 5
def main():
    """vowel"""
    str_ = input()
    # the input string is in s
    # remove pass and start your code here
    count_ = 0
    for letter_ in str_:
        if letter_ in ('a', 'e', 'i', 'o', 'u'):
            count_ = count_ + 1
    print(count_)
if __name__ == "__main__":
    main()
