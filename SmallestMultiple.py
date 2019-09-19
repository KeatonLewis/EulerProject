
import math

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range (3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i

    if n > 2:
        factors.append(int(n))
    return factors

factorized = [factorize(i) for i in range(2,21)]
finalFactors = []

for i in range(2,21):
    maxPower = 0
    for li in factorized:
        temp = 0
        for num in li:
            if num == i:
                temp += 1
        if temp > maxPower:
            maxPower = temp
    finalFactors.append(i ** maxPower)






    



print(finalFactors)
product = 1
for num in finalFactors:
    product *= num

print(product)