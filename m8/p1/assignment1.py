"""fact"""
def factorial(n_1):
    """fact"""
    if n_1 == 0 or n_1 == 1:
        return 1
    else:
        return n_1 * factorial(n_1-1)
def main():
    """fact"""
    a_1 = input()
    print(factorial(int(a)))    
if __name__== "__main__":
    main()
