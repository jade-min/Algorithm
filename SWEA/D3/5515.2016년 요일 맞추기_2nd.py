import sys
sys.stdin = open('5515.2016년 요일 맞추기_input.txt')

T = int(input())

daysOfMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first = 3

for tc in range(1, T+1):
    m, d = map(int, input().split())
    accumulationOfBeforeMonth = sum(daysOfMonth[1:m])
    result = (accumulationOfBeforeMonth + d + first) % 7

    print("#{} {}".format(tc, result))