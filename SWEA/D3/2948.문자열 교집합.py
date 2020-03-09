import sys
sys.stdin = open('2948.문자열 교집합_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    N_set = set((input().split()))
    M_set = set((input().split()))

    result = N_set & M_set
    answer = len(result)

    print("#{} {}".format(tc, answer))