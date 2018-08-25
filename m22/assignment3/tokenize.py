'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    lst = []
    data = string.split("")
    lst = lst.append(data)
    str1 = [lst.count(word) for word in lst]
    return(dict(zip(lst,str1)))      
def main():
    string = ""
    lines = int(input())
    for i in range(lines):
        string += input()
        string += '\n'
    print(tokenize(string))

if __name__ == '__main__':
    main()
