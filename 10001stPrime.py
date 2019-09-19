import math

# Assuming n is positive
def isPrime(n):
    if n <= 3:
        if n != 1:
            return True
    if n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 1
    while k < math.sqrt(n):
        if n % (6 * k + 1) == 0 or n % (6 * k - 1) == 0:
            if (6 * k + 1) == n or (6 * k - 1) == n:
                break
            return False
        k += 1
    return True

primes = [2, 3, 5, 7, 11, 13]
i = primes[-1] + 1
while len(primes) != 10001:
    if isPrime(i):
        primes.append(i)
    i += 1

print(primes[-1])
            
