import sys
sys.stdin = open('4047.영준이의 카드 카운팅_input.txt')

T = int(input())

for tc in range(1, T+1):
    S = input()
    cards = []
    element = ''

    spade = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13']
    dia = ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13']
    heart = ['H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09', 'H10', 'H11', 'H12', 'H13']
    clova = ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13']

    for s in S:
        element += s
        if len(element) == 3:
            cards.append(element)
            element = ''

    check = list(set(cards))
    check.sort()
    cards.sort()

    if check != cards:
        print("#{} ERROR".format(tc))

    else:
        checkLength = len(check)
        for i in range(checkLength):
            if check[i][0] == 'S':
                spade.remove(check[i])

            elif check[i][0] == 'D':
                dia.remove(check[i])

            elif check[i][0] == 'H':
                heart.remove(check[i])

            elif check[i][0] == 'C':
                clova.remove(check[i])

        spadeLength = len(spade)
        diaLength = len(dia)
        heartLength = len(heart)
        clovaLength = len(clova)

        print("#{} {} {} {} {}".format(tc, spadeLength, diaLength, heartLength, clovaLength))