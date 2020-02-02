import sys
sys.stdin = open('1228.암호문1_input.txt')

T = 10

for tc in range(1, T+1):
    lengthOfOriginalPW = int(input())
    originalPW = input().split()
    cntOfCommand = int(input())
    command = input().split()

    for idx, val in enumerate(command):
        if val == 'I':
            for i in range(int(command[idx+2])-1, -1, -1):
                originalPW.insert(int(command[idx+1]), int(command[idx+3+i]))
    print("#{} {}".format(tc, ' '.join(map(str, originalPW[:10]))))