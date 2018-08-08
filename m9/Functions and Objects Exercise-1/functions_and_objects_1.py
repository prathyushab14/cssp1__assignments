"""obj"""
def apply_to_each(L, f):
	"""obj"""
    L1 = ()
    for i in range(len(L)):
        L[i] = f(L[i])
        L1 = L1 + (L[i],)
    return L1
def main():
	"""ffunc"""
    data = input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))
if __name__ == "__main__":
    main()
