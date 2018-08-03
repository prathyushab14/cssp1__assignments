"""cube"""
def main():
    """cube"""
    x_1 = int(input())
    guess_1 = 0
    for guess_1 in range(abs(x_1)+1):
        if guess_1**3 >= abs(x_1):
            break
    if guess_1**3 != abs(x_1):
        print(x_1, 'is not a perfect cube')
    else:
        if x_1 < 0:
            guess_1 = -guess_1
        print(str(x_1) + ' is ' + 'a perfect cube'
if __name__ == "__main__":
    main()
