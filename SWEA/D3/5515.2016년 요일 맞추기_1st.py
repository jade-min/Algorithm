import sys
sys.stdin = open('5515.2016년 요일 맞추기_input.txt')

T = int(input())

for tc in range(1, T+1):
    m, d = map(int, input().split())
    answer = 0

    if m == 1 or m == 4 or m == 7:
        answer = (d+3) % 7

    elif m == 2 or m ==8:
        answer = (d+6) % 7

    elif m == 3 or m == 11:
        answer = d % 7

    elif m == 5:
        answer = (d+5) % 7

    elif m == 6:
        answer = (d+1) % 7

    elif m == 9 or m == 12:
        answer = (d+2) % 7

    elif m == 10:
        answer = (d+4) % 7

    print("#{} {}".format(tc, answer))