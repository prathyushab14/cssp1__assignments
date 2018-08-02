""" vowels count"""
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    """vowel"""
    s_ = input()
    # the input string is in s
    # remove pass and start your code here
    c_ = 0
    for letter_ in s:
        if letter_ == 'a' or letter_ == 'e' or letter_ == 'i' or letter_ == 'o' or letter_ == 'u':
            c_ = c_ + 1
    print(c_)
if __name__== "__main__":
	main()
