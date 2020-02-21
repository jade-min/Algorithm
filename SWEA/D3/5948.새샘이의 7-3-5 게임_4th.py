import sys
sys.stdin = open('5948.새샘이의 7-3-5 게임_input.txt')

T = int(input())

for tc in range(1, T+1):
    datas = list(map(int, input().split()))
    result = []

    for data1 in datas:
        data = [data1, 0, 0]
        for data2 in datas:
            if not data2 in data:
                data[1] = data2
            for data3 in datas:
                if not data3 in data:
                    data[2] = data3
                if sum(data) not in result:
                    result.append(sum(data))

    result.sort()
    print("#{} {}".format(tc, result[-5]))