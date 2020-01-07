import sys
sys.stdin = open('1215.회문1_input.txt')

def check_by_row(r1, c1):
    r_cnt = 0
    check1 = board[r1][c1:c1+palindrome_length]

    for i in range(palindrome_length//2):
        if check1[i] == check1[palindrome_length-i-1]:
            r_cnt += 1
        else:
            break

    if r_cnt == palindrome_length//2:
        return 1
    
    else:
        return 0

def check_by_col(r2, c2):
    c_cnt = 0
    check2 = board_by_col[r2][c2:c2+palindrome_length]

    for j in range(palindrome_length//2):
        if check2[j] == check2[palindrome_length-j-1]:
            c_cnt += 1
        else:
            break

    if c_cnt == palindrome_length//2:
        return 1
    
    else:
        return 0

T = 10

for tc in range(1, T+1):
    palindrome_length = int(input())
    board = [[0 for _ in range(8)] for _ in range(8)]
    board_by_col = [[0 for _ in range(8)] for _ in range(8)]
    row_cnt = 0
    col_cnt = 0
    for origin_row in range(8):
        board[origin_row] = list(input())

    for col in range(8):
        for row in range(8):
            board_by_col[col][row] = board[row][col]

    for r1 in range(8):
        for c1 in range(8-palindrome_length+1):
            row_cnt += check_by_row(r1, c1)

    for r2 in range(8):
        for c2 in range(8-palindrome_length+1):
            col_cnt += check_by_col(r2, c2)

    print("#{} {}".format(tc, row_cnt + col_cnt))
