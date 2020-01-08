import sys
sys.stdin = open('1220.Magnetic_input.txt')

T = 10

for tc in range(1, T+1):
    tableLength = int(input()) # 정사각형 테이블의 한 변의 길이
    table = [[0 for x in range(tableLength)] for y in range(tableLength)] # 테이블 초기화

    # 테스트 케이스 입력받기
    for i in range(tableLength):
        table[i] = list(input().split())

    # 교착 개수 초기화
    cnt = 0

    # 2차원 배열을 세로로 탐색
    for col in range(tableLength):
        
        newY = 0 # 세로열에서 움직일 좌표 초기화

        for row in range(tableLength-1):

            # 좌표가 테이블 크기를 벗어나거나 같으면 옆의 세로열로 이동
            if newY >= tableLength-1:
                break

            # 세로열에서 현재위치와 바로 밑의 위치가 같은 성질을 띄는 자성체 또는 빈 칸일 때는
            elif table[newY][col] == table[newY+1][col]:
                newY += 1 # 세로열에서 움직일 좌표를 바로 밑의 위치로 이동

            # 세로열에서 현재위치가 빈 칸, 바로 밑의 위치가 S극을 띄는 자성체일 때는
            elif table[newY][col] == "0" and table[newY+1][col] == "2":
                # S극 자성체는 제일 위에 있는 N극으로 향하려는 성질이므로 한 칸 위로 당겨준다
                table[newY][col], table[newY+1][col] = "2", "0"
                newY += 1 # 그리고 세로열에서 움직일 좌표를 바로 밑의 위치로 이동

            # 세로열에서 현재위치가 N극을 띄는 자성체, 바로 밑의 위치가 빈 칸일 때는
            elif table[newY][col] == "1" and table[newY+1][col] == "0":
                # N극 자성체는 제일 밑에 있는 S극으로 향하려는 성질이므로 한 칸 위로 당겨준다
                table[newY][col], table[newY+1][col] = "0", "1"
                newY += 1 # 그리고 세로열에서 움직일 좌표를 바로 밑의 위치로 이동

            # 세로열에서 현재위치가 N극을 띄는 자성체, 바로 밑의 위치가 S극을 띄는 자성체일 때는
            elif table[newY][col] == "1" and table[newY+1][col] == "2":
                cnt += 1 # 교착이 일어났으므로 교착의 갯수를 카운팅한 뒤
                newY += 2 # 세로열에서 움직일 좌표를 교착 덩어리 바로 밑의 위치로 이동
     
            # 나머지 경우들은 위의 경우들과 중복 혹은 교착이 일어나는 경우와 상관이 없으므로
            else:
                newY += 1 # 세로열에서 움직일 좌표를 바로 밑의 위치로 이동

    print("#{} {}".format(tc, cnt))