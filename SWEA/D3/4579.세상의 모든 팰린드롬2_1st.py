import sys
sys.stdin = open('4579.세상의 모든 팰린드롬2_input.txt')

def check(data):
    dataLength = len(data) // 2
    answer = "Exist"

    for i in range(dataLength):
        if data[i] == "*" or data[-(i+1)] == "*":
            break

        if data[i] != data[-(i+1)]:
            answer = "Not exist"
            break

    return answer


T = int(input())

answers = [0] * T

for tc in range(1, T+1):
    data = input()
    answers[tc-1] = "#{} {}".format(tc, check(data))
answer = '\n'.join(answers)
print(answer)
    # print("#{} {}".format(tc, check(data)))