import sys
sys.stdin = open('4751.다솔이의 다이아몬드 장식_input.txt')

def diamondDecoration(char, i):
    decoration = [['.' for _ in range(5)] for _ in range(5)]

    for row1 in range(3):
        decoration[row1][2-row1] = '#'
        for col1 in range(row1):
            if col1 == 0:
                decoration[col1+1][col1+3] = '#'
            else:
                decoration[col1+1][(col1+1)*2] = '#'

    for row2 in range(3, 5):
        decoration[row2][row2-2] = '#'
        for col2 in range(row2//2):
            if row2//2 == 1:
                decoration[row2][col2+3] = '#'

    decoration[2][2] = char[i]

    return decoration

T = int(input())

for tc in range(1, T+1):
    char = input()
    lengthOfChar = len(char)

    answer = [[], [], [], [], []]
    for i in range(lengthOfChar):
        for j in range(5):

            if i != lengthOfChar-1:
                for x in range(4):
                    answer[j].append(diamondDecoration(char, i)[j][x])

            else:
                for y in range(5):
                    answer[j].append(diamondDecoration(char, i)[j][y])

    for a in answer:
        print(''.join(a))