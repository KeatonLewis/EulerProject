import math

def isPythag(a, b, c):
    return a**2 + b**2 == c**2

n = 1000

a = b = c = 1
# this is super inefficient
while c < n:
    while b < c:
        while a < b:
            if a + b + c == 1000 and isPythag(a, b, c):
                print(a*b*c)                
            a += 1
        a = 1       
        b += 1
    b = 1
    c +=1
