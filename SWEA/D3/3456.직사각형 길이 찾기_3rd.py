import sys
sys.stdin = open('3456.직사각형 길이 찾기_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))

    answer = 0
    for el in data:
        if data.count(el) % 2:
            answer = el      

    print("#{} {}".format(tc, answer))