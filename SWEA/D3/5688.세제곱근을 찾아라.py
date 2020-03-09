import sys
sys.stdin = open('5688.세제곱근을 찾아라_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    calculation = int(round(N ** (1/3), 5))

    if (calculation**3) == N:
        print("#{} {}".format(tc, calculation))
    else:
        print("#{} -1".format(tc))