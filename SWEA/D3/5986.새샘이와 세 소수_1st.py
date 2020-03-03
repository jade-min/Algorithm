import sys
sys.stdin = open('5986.새샘이와 세 소수_input.txt')

T = int(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

for x in range(60, 1000):
    flag = True
    k = int(x ** (0.5))
    for y in range(2, k+1):
        if x % y == 0:
            flag = False
            break
        
    if flag:
        primes.append(x)

lengthOfPrimes = len(primes)

results = [0] * T

for tc in range(1, T+1):
    N = int(input())

    cnt = 0
    for i in range(lengthOfPrimes):
        for j in range(i, lengthOfPrimes):
            for k in range(j, lengthOfPrimes):
                if primes[i] + primes[j] + primes[k] == N:
                    cnt += 1

    results[tc - 1] = "#{} {}".format(tc, cnt)
answer = ('\n').join(results)
print(answer)