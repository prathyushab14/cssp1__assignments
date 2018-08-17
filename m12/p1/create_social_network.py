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
    # str1 = data
    # str1 = str1.split(" follows ")
    # dict1_ = {}
    # for i in str1:
    #     if i not in dict1_:
    #         dict1_[i] = list(i[1])
    #     else:
    #         dict1_[i] = dict1_.append([0])
    # return dict1_
    dict1 = {}
    def slomosplit(data):
        if "follows" not in data:
            return dict1
        data = data.split(" follows ")
        if data[0] not in dict1:
            dict1[data[0]] = data[1].split(',')
        else:
            #print(data)
            dict1[data[0]] += data[1].split(',')
        return dict1
    splitline = data.splitlines()
    for i in splitline:
        slomosplit(i)
    return dict1
def main():
    """handling test cases"""
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(create_social_network(string))
if __name__ == "__main__":
    main()
