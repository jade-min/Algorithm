import sys
sys.stdin = open('3750.Digit sum_input.txt')

T = int(input())
answers = [0] * (T+1)
for tc in range(1, T+1):
    N = input()
    nLength = len(N)

    result = 0
    i = 1
    while True:
        N = int(N)
        result += N % 10
        N = N // 10
        i += 1
        if N == 0:
            if len(str(result)) != 1:
                N = result
                result, i = 0, 1
            else:
                break
    answers[tc] = "#{} {}".format(tc, str(result))
answer = '\n'.join(answers[1:])
print(answer)