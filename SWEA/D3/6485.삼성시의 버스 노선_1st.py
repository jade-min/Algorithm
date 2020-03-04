import sys
sys.stdin = open('6485.삼성시의 버스 노선_input.txt')

T = int(input())

answers = [0] * T

for tc in range(1, T+1):
    N = int(input())
    busStop = {}
    for n in range(N):
        A, B = map(int, input().split())
        check = range(A, B+1)
        for c in check:
            if c not in busStop:
                busStop[c] = 1
            else:
                busStop[c] += 1

    P = int(input())
    result = "#{}".format(tc)
    for p in range(1, P+1):
        C = int(input())
        if C not in busStop:
            busStop[C] = 0
        result += " {}".format(busStop[C])
    answers[tc-1] = result
answer = '\n'.join(answers)
print(answer)