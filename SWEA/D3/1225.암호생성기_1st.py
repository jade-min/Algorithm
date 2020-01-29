import sys
sys.stdin = open("1225.암호생성기_input.txt")

T = 10

for tc in range(1, T+1):
    tcNum = int(input())
    data = list(map(int, input().split()))

    loop = max(data)
    flag = 0
    for i in range(loop):
        if flag == 1:
            break
        tail = 0
        for j in range(1, 6):
            tail = data[0] - j
            if tail <= 0:
                tail = 0
            data.remove(data[0])
            data.append(tail)
            if tail == 0:
                flag = 1
                break

    print("#{} ".format(tc), end="")
    for k in range(len(data)):
        print("{} ".format(data[k]), end="")
    print()