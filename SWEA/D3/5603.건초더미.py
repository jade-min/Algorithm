import sys
sys.stdin = open('5603.건초더미_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    hay = []

    for n in range(N):
        Si = int(input())
        hay.append(Si)

    hay.sort(reverse=True)
    total = sum(hay)
    average = total // N

    answer = 0
    for i in range(N):
        if hay[i] > average:
            answer += hay[i] - average
        else:
            break

    print("#{} {}".format(tc, answer))