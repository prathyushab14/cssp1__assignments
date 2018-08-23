"""matrix"""
def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = []
    if len(m1_[0]) == len(m2_):
        for i1_ in range(len(m1_)):
            restemp = []
            for j1_ in range(len(m2_[0])):
                res = 0
                for k1_ in range(len(m2_)):
                    res += m1_[i1_][k1_] * m2_[k1_][j1_]
                restemp.append(res)
            result.append(restemp)
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return
def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    #for i,j in zip(m1,m2)
        #if len(m1) == len(m2):
    #
    if len(m1_) != len(m2_): 
        print("Error: Matrix shapes invalid for addition")
        return
    for i1_, j1_ in zip(m1_, m2_):
        if len(i1_) != len(j1_):
            print("Error: Matrix shapes invalid for addition")
            return
    else:
        m3_ = [[m1_[i1_][j1_] + m2_[i1_][j1_] for j1_ in range(len(m1_[0]))] for i1_ in range(len(m1_))]
        return m3_
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows, columns = input().split(",")
    # print(rows,columns)
    row = int(rows)
    column = int(columns)
    matrix = []
    for i1_ in range(row):
        lst = [int(i1_) for i1_ in input().split(" ")]
        matrix.append(lst)
        if len(lst) != column:
            print("Error: Invalid input for the matrix")
            return None
    return matrix 
def main():
    """main"""
    # read matrix 1

    m1_ = read_matrix()
    # read matrix 2
    m2_ = read_matrix()

    # add matrix 1 and matrix 2
    if (m1_ != None and m2_ != None):
        print(add_matrix(m1_, m2_))

    # multiply matrix 1 and matrix 2
    if (m1_ != None and m2_ != None):
        print(mult_matrix(m1_, m2_))
   

if __name__ == '__main__':
    main()
