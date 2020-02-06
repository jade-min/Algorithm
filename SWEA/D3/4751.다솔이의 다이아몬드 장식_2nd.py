import sys
sys.stdin = open('4751.다솔이의 다이아몬드 장식_input.txt')

T = int(input())

for tc in range(1, T+1):
    char = input()
    lengthOfChar = len(char)
    firstLine = '.' + ('.#..' * lengthOfChar)
    secondLine = '.' + ('#.' * 2 * lengthOfChar)
    thirdLine = '#'
    for i in range(lengthOfChar):
        thirdLine += '.' + char[i] + '.#'

    print(firstLine)
    print(secondLine)
    print(thirdLine)
    print(secondLine)
    print(firstLine)