""" vowels count"""
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    """vowel"""
    s = input()
    # the input string is in s
    # remove pass and start your code here
    c = 0
    for letter in s:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            c = c + 1
    print(c)
if __name__== "__main__":
	main()
