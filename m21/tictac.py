def main():
    rows, columns = 3, 3
    row = int(rows)
    column = int(columns)
    # print(row)
    # print(column)
    board = []
    for i in range(row):
        lst = [i for i in input().split(" ")]
        board.append(lst)
    print(decide_winner(board))
def decide_winner(board):
    for i in board:
        if i.count('o') == 3:
            return 'o'
        if i.count('x') == 3:
            return 'x'
        if i[0] == 'x':
            return 'x'
        if i[0] == 'o':
            return 'o'
if __name__ == '__main__':
    main()
