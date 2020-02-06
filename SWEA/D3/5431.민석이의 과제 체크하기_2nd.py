import sys
sys.stdin = open('5431.민석이의 과제 체크하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))

    answer = ''
    for i in range(1, N+1):
        if i not in submit:
            answer += str(i) + ' '

    print("#{} {}".format(tc, answer))