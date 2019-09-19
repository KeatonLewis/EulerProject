sum = 0

n1 = 1
n2 = 1
n3 = 0
i = 0
while n3 <= 4000000:
    n3 = n1 + n2
    if n3 % 2 == 0:
        sum += n3
    n1 = n2
    n2 = n3


print(sum)