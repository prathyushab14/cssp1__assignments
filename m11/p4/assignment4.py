"""Exercise: Assignment-4"""
def calculate_hand_len(hand1_):
    """sum"""
    sum1_ = 0
    for i_1 in hand1_.keys():
        sum1_ = sum1_ + hand1_[i_1]
    return sum1_
def main():
    """sum"""
    n_1 = int(input())
    adict = {}
    i_1 = 0
    while i_1 < n_1:
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
        i_1 += 1
    print(calculate_hand_len(adict))
if __name__ == "__main__":
    main()
