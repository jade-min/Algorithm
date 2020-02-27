import sys
sys.stdin = open('4047.영준이의 카드 카운팅_input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()
    dataLen = len(data)
    S, D, H, C = 13, 13, 13, 13

    cards = []
    card = ''
    for i in range(0, dataLen, 3):
        if i % 3 == 0:
            card = data[i] + data[i+1] + data[i+2]
            if card not in cards:
                cards.append(card)
            else:
                card = 'ERROR'
                break
                
    if card == 'ERROR':
        print("#{} ERROR".format(tc))
        
    for c in cards:
        if c[0] == 'S':
            S -= 1

        elif c[0] == 'D':
            D -= 1

        elif c[0] == 'H':
            H -= 1
        
        elif c[0] == 'C':
            C -= 1
            
    if card != 'ERROR':
        print("#{} {} {} {} {}".format(tc, S, D, H, C))