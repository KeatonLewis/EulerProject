import math

factors = []
n = 600851475143
while n % 2 == 0:
    factors.append(2)
    n = n / 2

for i in range (3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        factors.append(i)
        n = n / i

if n > 2:
    factors.append(n)

# Might need to sort the list first?
print(factors[-1])