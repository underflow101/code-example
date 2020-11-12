def fill_boarder_with_one(board):
    n = len(board)
    m = len(board[0])
    new_board = [[1] * (m+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            new_board[i+1][j+1] = board[i][j]
    return new_board