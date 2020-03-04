import sys
sys.stdin = open('6485.삼성시의 버스 노선_input.txt')

T = int(input())

answers = [0] * T

for tc in range(1, T+1):
    N = int(input())
    busStop = [0] * 5001
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            busStop[i] += 1

    P = int(input())
    result = "#{}".format(tc)
    for p in range(P):
        result += " {}".format(busStop[int(input())])
    answers[tc-1] = result
answer = '\n'.join(answers)
print(answer)