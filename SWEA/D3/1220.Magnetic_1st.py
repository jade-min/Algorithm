import sys
sys.stdin = open("1220.Magnetic_input.txt")

T = 1

for tc in range(1, T+1):
    tableLength = int(input()) # 정사각형 테이블의 한 변의 길이
    table = [[0 for x in range(tableLength)] for y in range(tableLength)] # 테이블 초기화

    # 테스트 케이스 입력받기
    for i in range(tableLength):
        table[i] = list(input())

    cnt = 0
    for col in range(tableLength):
        for row in range(tableLength-1):
            newX = row
            newY = col
            if table[newX][col] == "1":
                for idx1 in range(newX, tableLength):
                    if table[][col] == "2":
                        cnt += 1
                        newX = idx + 1
                        for idx2 in range(tableLength-newX)
                    
            elif table[newX][col] == "2" and table[newX+idx][col] == "1":
                cnt += 1
                newX = 1