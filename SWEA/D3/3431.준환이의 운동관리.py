import sys
sys.stdin = open('3431.준환이의 운동관리_input.txt')

T = int(input())

for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    result = 0

    if X > U:
        result = -1
    
    elif X < L:
        result = L-X

    else:
        result = 0

    print("#{} {}".format(tc, result))