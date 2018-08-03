"""cube"""# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
def main():
	"""cube"""
	# input is captured in s
    x_c = input()
    for guess_1 in range(abs(x_c)+1):
        if guess_1**3 >= abs(x_c):
            break
        if guess_1**3 != abs(x_c):
            print(x_c, 'is not a perfect cube')
        else:
            if x_c < 0:
                guess_1 = -guess_1
            print('cube root of' + str(x_c) + ' is ' + str(guess_1))
if __name__ == "__main__":
    main()
