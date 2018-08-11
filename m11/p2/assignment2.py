"""Exercise: Assignment-2"""
def update_hand(hand1_, word1_):
    """a2"""
    hand_n = dict(hand1_)
    for i in word1_:
        if i in hand1_.keys():
            hand_n[i] = hand_n[i] - 1
    return hand_n
def main():
    """string"""
    n_1 = input()
    adict_1 = {}
    for i in range(int(n_1)):
        data = input()
        i = i
        l_1 = data.split(" ")
        adict_1[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict_1, data1))
if __name__ == "__main__":
    main()