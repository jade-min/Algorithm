import sys
sys.stdin = open('3499.퍼펙트 셔플_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deck = list(input().split())
    result = [0 for k in range(N)]
    half = N//2
    oddLength = (N-1)//2

    if N % 2:
        result[-1] = deck.pop(half)

        for i in range(oddLength):
            result[2*i] = deck[i]
            result[(2*i)+1] = deck[half+i]

    else:
        for j in range(half):
            result[2*j] = deck[j]
            result[(2*j)+1] = deck[half+j]

    answer = ' '.join(result)
    print("#{} {}".format(tc, answer))