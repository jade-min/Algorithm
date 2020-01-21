import sys
sys.stdin = open('3314.보충학습과 평균_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))

    for i in range(5):
        if data[i] < 40:
            data[i] = 40

    result = sum(data) // 5

    print("#{} {}".format( tc, result ) )