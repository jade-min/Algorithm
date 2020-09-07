import sys
sys.stdin = open('10200.구독자 전쟁_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    maximum = 0 # maximum = min(A, B)
    if A > B:
        maximum = B
    else:
        maximum = A

    minimum = A + B - N
    if minimum <= 0:
        minimum = 0

    print("#{} {} {}".format(tc, maximum, minimum))