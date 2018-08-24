def main():
    rows, columns = 3, 3
    row = int(rows)
    column = int(columns)
    print(row)
    print(column)
    board = []
    for i in range(row):
	    lst = [i for i in input().split(" ")]
	    board.append(lst)
    print(decide_winner(board))
def decide_winner(board):
    for i in board:
    	if i.count(X) == 3:
    		return X
if __name__ = '__main__':
	main()
