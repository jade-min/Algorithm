primes = [2,3,5,7]

for i in range(10, 1000001):
    flag = True
    k = int(i ** 0.5)
    for j in range(2, k+1):
        if i % j == 0:
            flag = False
            break
    
    if flag:
        primes.append(i)

answer = " ".join(map(str, primes))
print(answer)