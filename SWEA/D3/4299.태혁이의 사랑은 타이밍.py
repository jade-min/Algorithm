import sys
sys.stdin = open('4299.태혁이의 사랑은 타이밍_input.txt')

T = int(input())

for tc in range(1, T+1):
    D, H, M = map(int, input().split())

    checkTotal = ((D - 11) * 24 * 60) + ((H - 11) * 60) + (M - 11)

    if checkTotal < 0:
        checkTotal = -1

    print("#{} {}".format(tc, checkTotal))