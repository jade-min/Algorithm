import sys
sys.stdin = open('3499.퍼펙트 셔플_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deck = list(input().split())
    result = []

    if N % 2:
        deck1 = deck[:(N//2)+1]
        deck2 = deck[(N//2)+1:]

        for i in range(len(deck2)):
            result.append(deck1[i])
            result.append(deck2[i])

        result.append(deck1[-1])

    else:
        deck1 = deck[:N//2]
        deck2 = deck[N//2:]

        for j in range(len(deck2)):
            result.append(deck1[j])
            result.append(deck2[j])

    answer = ' '.join(result)
    print("#{} {}".format(tc, answer))