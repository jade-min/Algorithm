import sys
sys.stdin = open('1217.거듭 제곱_input.txt')

def DFS(base, exponent):
    if exponent == 1:
        return base
    else:
        return base * DFS(base, exponent-1)

T = 10

for tc in range(1, T+1):
    testCaseNum = int(input())
    base, exponent = map(int, input().split())
    result = DFS(base, exponent)
    print("#{} {}".format(tc, result))