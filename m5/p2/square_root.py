# Write a python program to find the square root of the given number 
# using approximation method

def main():
	s = raw_input()
	 """square"""
    squ_ = int(input())
    eps_ = 0.01
    guess_ = 0.0
    cla_ = 0
    increment_ = 0.1
    num_guesses = 0
    while abs(guess_**2 - squ_) >= eps_:
        guess_ += increment_
        num_guesses += 1
    if abs(guess_**2 - squ_) >= eps_:
        cla_ = cla_+1
    else:
        print(str(guess_))
if __name__ == "__main__":
    main()