#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
def squ(x):
    s = x**2
    return s

def apply_to_each(L, f):
	L1 = ()
	for i in range(len(L)):
		L[i] = f(L(i))
		L1 = L1 + (L[i],)
    return L1    
    
def main():
	data = input()
    data = data.split()
    list1 = []
    for j in l:
        list1.append(int(j))
	apply_to_each(list1, square)

if __name__== "__main__":
	main()