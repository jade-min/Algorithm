import sys
sys.stdin = open('1208.Flatten_input.txt')

def dumping(maximum, minimum):
    for x in range(lengthOfBox):
        if box[x] == maximum:
            box[x] -= 1
            break

    for y in range(lengthOfBox):
        if box[y] == minimum:
            box[y] += 1
            return

T = 10

for tc in range(1, T+1):
    countOfDump = int(input())
    box = list(map(int, input().split()))
    lengthOfBox = len(box)

    for i in range(countOfDump):
        maximum = max(box)
        minimum = min(box)
        dumping(maximum, minimum)

    answer = max(box) - min(box)
    print("#{} {}".format(tc, answer))