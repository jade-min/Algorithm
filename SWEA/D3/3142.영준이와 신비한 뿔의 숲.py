import sys
sys.stdin = open('3142.영준이와 신비한 뿔의 숲_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    unicorn = 2*M-N
    twinhorn = N-M
    print("#{} {} {}".format(tc, unicorn, twinhorn))