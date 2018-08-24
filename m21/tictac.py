rows, columns = 3, 3
row = int(rows)
column = int(columns)
print(row)
print(column)
board = []
for i in range(row):
	lst = [i for i in input().split(" ")]
	board.append(lst)
print(board)