'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


# def word_list(text):
#     '''
#         Change case to lower and split the words using a SPACE
#         Clean up the text by remvoing all the non alphabet characters
#         return a list of words
#     '''
#     # word = text.lower()
#     # result = re.compile('[^a-z]')
#     # result1 = [result.sub("",w.strip()) for w in word.split(" ")]
#     # return result1
#     word = text.lower()
#     word1 = word.split(" ")
#     words = []
#     for w in word1:
#         words.append(w.strip())
#     regex = re.compile('[^a-z]')
#     word1s = [regex.sub("",w) for w in words]
#     return word1s
def find_keys(docs):


    counter = {i:docs.count(i) for i in docs}
    for a in counter.keys():
        if counter[a] > 1:
            return a
    
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    docs1 = " ".join(str(x) for x in docs)
    regex = re.compile('[^a-z]')

    words1 =[regex.sub("",w.strip()) for w in docs1.lower().split(" ")]
    counter = {i:docs.count(i) for i in docs}
    str1 = ""
    for a in counter.keys():
        if counter[a] > 1:
            str1 += a
    dict1 = {}
    stopwords = load_stopwords("stopwords.txt")
    # docs1 = word_list(docs)
    for w in words1:
        if w not in stopwords and len(w)>0:
            if w not in dict1.keys():
                dict1[w] = [0,0]
            dict1[w][1] += 1
    return print_search_index(w)

            



    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
# import re
# text = "comp%uters are efficie$nt3\n computers are"
# text = text.lower()
# print(text)
# result = re.compile('[^a-z]') 
# result1= [result.sub("",w.strip()) for w in text.split(" ")]
# print(result1)
# counter = {i:result1.count(i) for i in result1}
# print(counter)
# str1 = ""
# for a in counter.keys():
#     if counter[a] > 1:
#         str1 += a
# dict1 = {}
# # stopwords = load_stopwords("stopwords.txt")
# # docs = word_list(word)
# for w in result1:
#     # if w not in stopwords and len(w)>0:
#     if w not in dict1.keys():
#         dict1[w] = [0,0]
#     dict1[w][1] += 1
# print(dict1)
# # keys = "are"
# for i in dict1:
#         # if i in keys:
#     if i in str1:
#         print(i, "-" , dict1[i])
