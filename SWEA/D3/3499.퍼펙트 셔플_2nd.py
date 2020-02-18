import sys
sys.stdin = open('3499.퍼펙트 셔플_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deck = list(input().split())
    result = []
    half = N // 2

    if N % 2:
        deck1 = deck[:half+1]
        deck2 = deck[half+1:]

    else:
        deck1 = deck[:half]
        deck2 = deck[half:]

    for i in range(len(deck2)):
        result.append(deck1[i])
        result.append(deck2[i])

    if N % 2:
        result.append(deck1[-1])

    answer = ' '.join(result)
    print("#{} {}".format(tc, answer))