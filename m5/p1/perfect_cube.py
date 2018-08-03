"""cube"""
def main():
	"""input is captured in s"""
    x_1 = int(input())
    for guess_1 in range(abs(x_1)+1):
        if guess_1**3 >= abs(x_1):
            break
        if guess_1**3 != abs(x_1):
            print(x_1, 'is not a perfect cube')
        else:
            if x_1 < 0:
                guess_1 = -guess_1
            print('cube root of' + str(x_1) + ' is ' + str(guess_1))
if __name__ == "__main__":
    main()
