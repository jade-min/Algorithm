import sys
sys.stdin = open('1216.회문2_input.txt')

def RowCheck(board):
    rowResult = -987654321
    for row1 in range(100):
        for x in range(100):
            checkRow = ''
            for col1 in range(x, 100):
                checkRow += board[row1][col1]
                checkRowLength = len(checkRow)
                if checkRow == checkRow[::-1]:
                    if rowResult < checkRowLength:
                        rowResult = checkRowLength

    return rowResult

def ColCheck(board):
    colResult = -987654321
    for row2 in range(100):
        for y in range(100):
            checkCol = ''
            for col2 in range(y, 100):
                checkCol += board[col2][row2]
                checkColLength = len(checkCol)
                if checkCol == checkCol[::-1]:
                    if colResult < checkColLength:
                        colResult = checkColLength

    return colResult

T = 10
answers = [0] * T

for tc in range(1, T+1):
    N = input()
    board = [0] * 100
    for i in range(100):
        board[i] = list(input())

    result = max(RowCheck(board), ColCheck(board))
    answers[tc-1] = "#{} {}".format(tc,result)
answer = '\n'.join(answers)
print(answer)

