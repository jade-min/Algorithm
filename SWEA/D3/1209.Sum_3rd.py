import sys
sys.stdin = open('1209.Sum_input.txt')

def maxOfRowSumAndColSum():
    rowSum, colSum = 0, 0
    for row in range(100):
        rowSumCheck, colSumCheck = 0, 0

        for col in range(100):
            rowSumCheck += data[row][col]
            colSumCheck += data[col][row]

        if rowSumCheck > rowSum:
            rowSum = rowSumCheck

        if colSumCheck > colSum:
            colSum = colSumCheck

    return max(rowSum, colSum)

def diagonalSum():
    diagonal1, diagonal2 = 0, 0
    for x in range(100):
        diagonal1 += data[x][x]
        diagonal2 += data[x][99-x]

    return max(diagonal1, diagonal2)

T = 10

for tc in range(1, T+1):
    dummy = input()
    data = [0 for _ in range(100)]

    for i in range(100):
        data[i] = list(map(int, input().split()))

    answer = max(maxOfRowSumAndColSum(), diagonalSum())

    print("#{} {}".format(tc, answer))