import sys
sys.stdin = open("1213.String_input.txt", "rt", encoding="UTF-8")

T = 10

for tc in range(1, T+1):
    testCaseNum = input()
    checkChar = input()
    data = input()

    lengthOfCheckChar = len(checkChar)
    lengthOfData = len(data)

    cnt = 0
    for i in range(lengthOfData-lengthOfCheckChar+1):
        if data[i:i+lengthOfCheckChar] == checkChar:
            cnt += 1

    print("#{} {}".format(tc,cnt))