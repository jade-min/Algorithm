import sys
sys.stdin = open('1234.비밀번호_input.txt')

T = 10

for tc in range(1, T+1):
    originPasswordLength, originPassword = input().split() # 주어진 testCase 입력받기
    originPassword = list(originPassword) # 문제 풀기 위해 list 로 변환

    i = 0
    while True:
        if i == len(originPassword)-1: # 탈출 조건 : 끝 - 1 까지 다 왔는가
            if originPassword[i] == originPassword[i-1]: # 끝 - 1 과 끝이 같다면 제거하고 
                originPassword.pop(i)
                originPassword.pop(i)
            break # 탈출

        if i == 0: # 시작점일 때
            if originPassword[i] == originPassword[i+1]: # 시작점과 바로 다음 것이 같으면 제거
                originPassword.pop(i)
                originPassword.pop(i)
                i -= 1 # 제거하고 index 다시 당겨줘야지
            i += 1 # 다르면 index 한 칸 전진
        
        else: # 2번째부터
            if originPassword[i] == originPassword[i+1] or originPassword[i] == originPassword[i-1]: # 뒤 또는 앞이 같으면 같은 것 제거
                originPassword.pop(i)
                originPassword.pop(i)
                i -= 1

            else: # 다르면 그냥 index 한 칸 전진
                i += 1


    print("#{} {}".format(tc, ''.join(originPassword)))
