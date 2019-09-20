# This is a classic combinatorics problem
# You have to move right 20 times and down 20 times no matter what
# And as a result the answer is just 40 choose 20

def factorial(n):
    product = 1
    for  i in range(1, n + 1):
        product *= i
    
    return product

print(factorial(40) / (factorial(20) * factorial(40 - 20)))