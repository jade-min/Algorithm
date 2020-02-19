import sys
sys.stdin = open('5789.현주의 상자 바꾸기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for j in range(R-L+1):
            box[L-1+j] = i

    answer = ' '.join(map(str, box))
    print("#{} {}".format(tc, answer))