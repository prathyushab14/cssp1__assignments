'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dict1 = {}
    for word in string:
        if word in dict1.keys():
            dict1[word] += 1
        else:
            dict1[word] = 1
    return dict1   
def main():
    string = ""
    lines = int(input())
    for i in range(lines):
        string += input()
        string += '\n'
    print(string)
    print(tokenize(string))

if __name__ == '__main__':
    main()
