"""int"""
def integer_division(x1_, a1_):
    """div"""
    count1 = 0
    while x1_ >= a1_:
        count1 += 1
        x1_ = x1_ - a1_
    return count1
def main():
    """integer"""
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
