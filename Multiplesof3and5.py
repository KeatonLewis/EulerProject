multis = []

i = 1
while(True):
    temp = 3*i
    if(temp < 1000):
        i += 1
        multis.append(temp)
    else:
        break

i = 1
while(True):
    temp = 5*i
    if(temp < 1000):
        i += 1
        if(temp % 3 != 0):
            multis.append(temp)
    else:
        break

sum = 0
for num in multis:
    sum += num

print(sum)
