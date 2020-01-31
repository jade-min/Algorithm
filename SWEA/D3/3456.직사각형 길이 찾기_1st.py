import sys
sys.stdin = open('3456.직사각형 길이 찾기_input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    original = sorted([a, b, c])
    check = set(original)
    lenghtOfCheck = len(check)

    answer = 0
    if lenghtOfCheck == 1:
        answer = original[0]

    else:
        for i in range(1, 3):

            if original[0] == original[i]:
                answer = original[2]

            else:
                answer = original[0]

            break

    print("#{} {}".format(tc, answer))