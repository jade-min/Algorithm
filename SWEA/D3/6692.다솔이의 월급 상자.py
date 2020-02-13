import sys
sys.stdin = open('6692.다솔이의 월급 상자_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0
    for i in range(N):
        pi, xi = map(float, input().split())
        answer += pi*xi

    print("#{} {}".format(tc, answer))