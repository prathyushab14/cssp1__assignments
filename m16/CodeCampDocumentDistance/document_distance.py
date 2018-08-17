'''
    Document Distance - A detailed description is given in the PDF
'''
def remove_stop_words(words,stopwords):
    words1 = []
    words1 = words.copy()
    for w in words:
        if w not in stopwords and len(w)>0:
            words1.append(w)
    return words1

def words_list(doc):
    word = doc.lower()
    word = word.split("")
    words = []
    for w in word:
        words.append(w.strip())
    regex = re.compile("[^a-z]")
    words = [regex.sub(" ",w) for w in word]
    return words



def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    words_1 = words_list(dict1)
    words_2 = words_list(dict2)
    stopwords = load_stopwords("stopwords.txt")
    words1 = remove_stop_words(words_1,stopwords)
    words2 = remove_stop_words(words_2,stopwords)
    dictionary = dict()
    dictionary = createDictionary(dictionary,words_1,0)
    dictionary = createDictionary(dictionary,words_2,1)
def createDictionary(dictionary,words,index):
    for w in word:
        if w not in dictionary.keys()
            dictionary[w] = [0,0]
        dictionary[w][index] += 1
    return dictionary
def compute(dictionary):
    numerator = sum([v[0]*v[1] for v in dictionary.values()])
    denominator1 = math.sqrt(sum([v[0]**2 for v in dictionary.values()]))
    denominator2 = math.sqrt(sum([v[1]**2 for v in dictionary.values()]))
    return numerator/(denominator1 * denominator2)
    



def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
