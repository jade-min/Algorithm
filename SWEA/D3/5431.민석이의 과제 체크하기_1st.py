import sys
sys.stdin = open('5431.민석이의 과제 체크하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))

    studentTotalNum = list(range(1, N+1))

    answer = []
    for i in range(N):
        if studentTotalNum[i] not in submit:
            answer.append(studentTotalNum[i])

    print("#{}".format(tc), end="")
    for j in range(N-K):
        print(" {}".format(answer[j]), end="")
    print()