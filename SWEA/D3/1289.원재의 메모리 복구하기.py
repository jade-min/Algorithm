import sys
sys.stdin = open('1289.원재의 메모리 복구하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(input())
    originStatus = ["0"] * len(data) 

    cnt = 0
    for i in range(len(data)):

        if data[i] != originStatus[i]:
            originStatus[i:] = data[i] * (len(originStatus) - i)
            cnt += 1

        if data == originStatus:
            break

    print("#{} {}".format(tc, cnt))
