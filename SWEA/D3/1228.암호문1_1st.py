import sys
sys.stdin = open('1228.암호문1_input.txt')

T = 10

for tc in range(1, T+1):
    lengthOfOriginalPW = int(input())
    originalPW = list(map(int, input().split()))
    cntOfCommand = int(input())
    command = input().split()
    lengthOfCommand = len(command)

    for i in range(lengthOfCommand):
        if command[i] is 'I':
            part = command[i+3:i+3+int(command[i+2])][::-1]
            for j in range(len(part)):
                originalPW.insert(int(command[i+1]), part[j])

    answer = originalPW[:10]
    lengthOfAnswer = len(answer)
    print("#{} ".format(tc), end="")
    for k in range(lengthOfAnswer):
        print("{} ".format(answer[k]), end="")
    print()