'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """read input"""
    string = ""
    lines = int(input())
    for i in range(lines):
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
