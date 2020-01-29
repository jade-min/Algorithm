import sys
sys.stdin = open('1234.비밀번호_input.txt')

T = 10

for tc in range(1, T+1):
    originPasswordLength, originPassword = input().split() # 주어진 testCase 입력받기
    originPassword = list(originPassword) # 문제 풀기 위해 list 로 변환


    if originPassword[0] == originPassword[1]: # 시작점과 바로 다음 것이 같으면 제거
        originPassword.pop(0)
        originPassword.pop(0)

    i = 0 # 시작점부터 해결하고 첫 시작점 잡기

    while i != len(originPassword)-1: # 탈출 조건 : 끝 - 1 까지 다 왔는가

        if originPassword[i] == originPassword[i+1]: # 시작점이 아닌 지점과 그 바로 다음 것이 같다면 제거
            originPassword.pop(i)
            originPassword.pop(i)
            i -= 1 # 제거하고 index 다시 당겨주고

        else: # 다르면 index 한 칸 전진
            i += 1

    # while 탈출 조건에서 묻기 : 출력 전에 끝과 끝 - 1 이 같은지 확인
    if originPassword[i] == originPassword[i-1]: # 같다면 제거
        originPassword.pop(i)
        originPassword.pop(i)

    print("#{} {}".format(tc, ''.join(originPassword)))