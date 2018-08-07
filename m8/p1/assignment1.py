"""fact"""
def factorial(n):
    """fact"""
    if n == 0 or n == 1:
    	return 1
    else:
    	return n * factorial(n-1)
def main():
	"""fact"""
    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
