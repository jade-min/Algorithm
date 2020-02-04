import sys
sys.stdin = open('1206.View_input.txt')

T = 10

for tc in range(1, T+1):
    lengthOfBuilding = int(input())
    building = list(map(int, input().split()))

    answer = 0
    for i in range(2, lengthOfBuilding-2):
        check = building[i-2:i+3]
        if building[i] == max(check):
            answer += check.pop(2) - max(check)

    print("#{} {}".format(tc, answer))