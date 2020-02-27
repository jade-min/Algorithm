import sys
sys.stdin = open('1229.암호문2_input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    originPW = input().split()
    commandLen = int(input())
    command = input().split()
    commandLength = len(command)

    for i in range(commandLength):
        if command[i] == 'I':
            originPW = originPW[:int(command[i+1])] + command[i+3:i+3+int(command[i+2])] + originPW[int(command[i+1]):]

        elif command[i] == 'D':
            originPW = originPW[:int(command[i+1])] + originPW[int(command[i+1])+int(command[i+2]):]

    answer = ' '.join(originPW[:10])
    print("#{} {}".format(tc, answer))