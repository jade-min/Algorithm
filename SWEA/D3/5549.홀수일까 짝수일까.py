import sys
sys.stdin = open('5549.홀수일까 짝수일까_input.txt')

T = int(input())

for tc in range(1, T+1):
    positiveInteger = int(input())

    answer = 'Even'

    if positiveInteger % 2:
        answer = 'Odd'

    print('#{} {}'.format(tc, answer))