import sys
sys.stdin = open('5431.민석이의 과제 체크하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = map(int, input().split())

    students = [1] + [0] * N

    for student in submit:
        students[student] = 1

    answer = ''
    for idx, val in enumerate(students):
        if not val:
            answer += str(idx) + ' '

    print("#{} {}".format(tc, answer))