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
    diag1 = set([board[0][0],board[1][1],board[2][2]])
    diag2 = set([board[0][2].board[1][1],board[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and board[1][1] != '.':
        return board[1][1]
if __name__ == '__main__':
    main()
