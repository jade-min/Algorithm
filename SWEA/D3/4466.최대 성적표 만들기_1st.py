import sys
sys.stdin = open('4466.최대 성적표 만들기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    answer = 0
    scores.sort(reverse=True)
    for i in range(K):
        answer += scores[i]

    print("#{} {}".format(tc, answer))