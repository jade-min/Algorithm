import sys
sys.stdin = open("4406.모음이 보이지 않는 사람_input.txt")

T = int(input())

for tc in range(1, T+1):
    string = list(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    for char in string:
        if char not in vowels:
            result += char

    print("#{} {}".format(tc, result))