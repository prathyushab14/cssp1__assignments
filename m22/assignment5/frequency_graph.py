'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def frequency_graph(dictionary):
    """freq"""
    lst = list(dictionary.keys())
    lst.sort()
    for i1_ in lst:
        n1_ = dictionary[i1_]
        print(" - ".join((i1_, str(n1_ * "#"))))
def main():
    """input"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
