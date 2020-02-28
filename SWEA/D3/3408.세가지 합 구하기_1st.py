import sys
sys.stdin = open('3408.세가지 합 구하기_input.txt')

T = int(input())

answers = [0] * T

for tc in range(1, T+1):
    N = int(input())

    S1 = ( N * (N+1) ) // 2
    S2 = N ** 2
    S3 = N * (N+1)
    
    answers[tc-1] = "#{} {} {} {}".format(tc, S1, S2, S3)
answer = '\n'.join(answers)
print(answer)