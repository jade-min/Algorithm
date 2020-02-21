import sys
sys.stdin = open('5948.새샘이의 7-3-5 게임_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    result = set()
    for i in range(5):
        for j in range(i+1,6):
            for k in range(j+1,7):
                result.add(data[i]+data[j]+data[k])
    result = sorted(result)[-5]
    print("#{} {}".format(tc, result))