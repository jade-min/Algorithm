import sys
sys.stdin = open('3233.정삼각형 분할 놀이_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    answer = (A//B) ** 2 
    print("#{} {}".format(tc, answer))