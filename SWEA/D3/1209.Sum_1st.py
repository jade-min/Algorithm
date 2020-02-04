import sys
sys.stdin = open('1209.Sum_input.txt')

T = 10

for tc in range(1, T+1):
    dummy = input()
    data = [0 for _ in range(100)]

    for i in range(100):
        data[i] = list(map(int, input().split()))

    rowSum = 0
    for row1 in range(100):
        rowSumCheck = 0
        for col1 in range(100):
            rowSumCheck += data[row1][col1]
        if rowSumCheck > rowSum:
            rowSum = rowSumCheck

    colSum = 0
    for col2 in range(100):
        colSumCheck = 0
        for row2 in range(100):
            colSumCheck += data[row2][col2]
        if colSumCheck > colSum:
            colSum = colSumCheck

    diagonal1, diagonal2 = 0, 0
    for x in range(100):
        diagonal1 += data[x][x]

    for y in range(100):
        diagonal2 += data[y][99-y]
        
    answer = max(rowSum, colSum, diagonal1, diagonal2)

    print("#{} {}".format(tc, answer))