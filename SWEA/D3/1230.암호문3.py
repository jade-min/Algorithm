import sys
sys.stdin = open('1230.암호문3_input.txt')

T = 10

for tc in range(1, T+1):
    origin_pw_length = int(input())
    origin_pw = list(input().split())
    command_length = int(input())
    command = list(input().split())
    
    for i in range(len(command)):
        if command[i] == 'I':
            for j in range(int(command[i+2])):
                origin_pw.insert(int(command[i+1])+j, int(command[i+3+j]))

        elif command[i] == 'D':
            for k in range(int(command[i+2])):
                origin_pw.pop(int(command[i+1])+k)

        elif command[i] == 'A':
            for l in range(int(command[i+1])):
                origin_pw.append(int(command[i+2+l]))
    
    print("#{} {} {} {} {} {} {} {} {} {} {}".format(tc, origin_pw[0], origin_pw[1], origin_pw[2], origin_pw[3], origin_pw[4], origin_pw[5], origin_pw[6], origin_pw[7], origin_pw[8], origin_pw[9]))