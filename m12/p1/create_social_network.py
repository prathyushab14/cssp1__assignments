'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    # str1 = data
    # str1 = str1.split(" ")
    # len1 = len(str1)
    # dict_ = {}
    # for i in range(len(str1)):
    # 	for ele in i:
    # 	    if ele.split(',').data[0] not in dict_:
    # 		    ele.split(',').data[0]=list(ele.split(',').data[1])
    # 	    else:
    # 		    ele.split(',').data[0].append(ele.split(',').data[1])
    str1 = data
    str1 = str1.split("follows ")
    dict1_ = {}
    for i in str1:
        if i not in dict1_:
            dict1_[i] = list(i.split("\n"))
        else:
            dict1_[i] = dict1_.append([0])
    return dict1_

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
