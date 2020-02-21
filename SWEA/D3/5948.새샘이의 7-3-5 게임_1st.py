import sys
sys.stdin = open('5948.새샘이의 7-3-5 게임_input.txt')

from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    sums = list((permutations(data, 3)))
    result = []
    for i in range(len(sums)):
        result.append(sum(sums[i]))

    answer = list(set(result))
    answer.sort(reverse=True)
    print("#{} {}".format(tc, answer[4]))