import sys
sys.stdin = open('4579.세상의 모든 팰린드롬2_input.txt')

def check(data, dataReverse):
    dataLength = len(data) // 2
    answer = "Exist"

    for i in range(dataLength):
        if data[i] == "*" or dataReverse[i] == "*":
            break

        elif data[i] != dataReverse[i]:
            answer = "Not exist"
            break

    return answer

T = int(input())

answers = [0] * T

for tc in range(1, T+1):
    data = input()
    dataReverse = data[::-1]
    answers[tc-1] = "#{} {}".format(tc, check(data, dataReverse))
answer = '\n'.join(answers)
print(answer)
    # print("#{} {}".format(tc, check(data)))