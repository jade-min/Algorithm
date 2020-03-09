import sys
sys.stdin = open('4522.세상의 모든 팰린드롬_input.txt')

def check(data):
    dataLength = len(data)//2

    for i in range(dataLength):
        if data[i] == "?" or data[-(i+1)] == "?":
            continue
        if data[i] != data[-(i+1)]:
            return "Not exist"
    return "Exist"

T = int(input())

for tc in range(1, T+1):
    data = input()
    print("#{} {}".format(tc, check(data)))