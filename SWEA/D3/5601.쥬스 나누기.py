import sys
sys.stdin = open('5601.쥬스 나누기_input.txt')

T = int(input())

for tc in range(1, T+1):
    peopleNum = int(input())
    data = [("1/" + str(peopleNum))] * peopleNum

    print("#{} ".format(tc), end="")
    for i in range(peopleNum):
        print("{} ".format(data[i]), end="")
    print()