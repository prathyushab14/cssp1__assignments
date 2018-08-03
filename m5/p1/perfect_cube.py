# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
	# input is captured in s
    cube = input()
    for guess in range(abs(cube)+1):
        if guess**3 >= abs(cube):
    	    break
        if guess**3 != abs(cube):
    	    print(cube, 'is not a perfect cube')
        else:
    	    if cube < 0:
    		    guess = -guess
    	    print('cube root of' + str(cube) + ' is ' + str(guess))
if __name__== "__main__":
	main()
