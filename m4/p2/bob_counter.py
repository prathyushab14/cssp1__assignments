"""string"""
'''Assume s is a string of lower case characters.
Number of times bob occurs is: 2'''
def main():
    """string"""
    stri_ = input()
    str_ = 'bob'
    cou = 0
    for i in range(len(stri_)-2):
        if str_ == stri_[i]+stri_[i+1]+stri_[i+2]:
            cou = cou + 1
    print(cou)
if __name__== "__main__":
    main()
