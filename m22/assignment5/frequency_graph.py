'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    lst = list(dictionary.keys())
    lst.sort()
    for i in lst:
    	n = dictionary[i]
    	while n > 0:
    		dictionary[i] = "#"
        print(" - ".join((i, str(dictionary[i]))))

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
