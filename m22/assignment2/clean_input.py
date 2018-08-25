'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
	for i in string:
		string.append(i.strip())
	regex = re.compile('[^a-z]','[^A-Z]','[^0-9]')
    str1 = [regex.sub("",i) for i in string]
    return str1

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
