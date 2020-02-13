import sys
sys.stdin = open('5162.두가지 빵의 딜레마_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    if A > B:
        A, B = B, A
    
    answer = C // A

    print("#{} {}".format(tc, answer))