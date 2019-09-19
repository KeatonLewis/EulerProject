import math
def numOfDivisors(triNumber):
    divisorList = []
    for i in range(1, int(math.sqrt(triNumber) + 1)):
        if triNumber % i == 0:
            if triNumber / i == i:
                divisorList.append(i)
            else:
                divisorList.append(i)
                divisorList.append(triNumber / i)
    return len(divisorList)

divisors = 1
triNumber = [1]
while (divisors < 500):
    triNumber.append(triNumber[-1] + len(triNumber) + 1)
    divisors = numOfDivisors(triNumber[-1])

# This does take a little while but I'm not sure how much better it can be
print(triNumber[-1])