import sys
sys.stdin = open('2805.농작물 수확하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [0 for _ in range(N)]

    for i in range(len(board)):
        board[i] = list(map(int, input()))

    answer = 0
    for increase in range(N//2+1):
        answer += sum(board[increase][N//2-increase:N//2+increase+1])

    for decrease in range(N//2+1,N):
        answer += sum(board[decrease][decrease-N//2:N//2-decrease])

    print("#{} {}".format(tc, answer))