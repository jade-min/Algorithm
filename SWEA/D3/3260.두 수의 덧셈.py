import sys
sys.stdin = open('3260.두 수의 덧셈_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    answer = A + B
    print("#{} {}".format(tc, answer))