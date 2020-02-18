import sys
sys.stdin = open('3499.퍼펙트 셔플_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deck = list(input().split())
    result = [0 for k in range(N)]

    if N % 2:
        result [-1] = deck.pop(N//2)

        for i in range((N-1)//2):
            result[2*i] = deck[i]
            result[(2*i)+1] = deck[(N//2)+i]

    else:
        for j in range(N//2):
            result[2*j] = deck[j]
            result[(2*j)+1] = deck[(N//2)+j]

    answer = ' '.join(result)
    print("#{} {}".format(tc, answer))