import sys
sys.stdin = open('3233.정삼각형 분할 놀이_input.txt')

T = int(input())

answers = [0] * T
for tc in range(1, T+1):
    A, B = map(int, input().split())
    result = (A//B) ** 2 
    answers[tc-1] = "#{} {}".format(tc, result)
answer = '\n'.join(answers)
print(answer)