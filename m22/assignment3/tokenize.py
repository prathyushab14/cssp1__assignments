'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    """dic"""
    dict1 = {}
    str1 = string.strip("\n")
    regex = re.sub('[^a-zA-Z"]', "", string)
    data = str1.split(" ")
    for i in data:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1
def main():
    """input"""
    string = ""
    lines = int(input())
    for i in range(lines):
        string += input()
        string += '\n'
    print(tokenize(string))

if __name__ == '__main__':
    main()
