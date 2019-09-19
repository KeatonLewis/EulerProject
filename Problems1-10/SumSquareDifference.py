n = 100

sum = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        else:
            sum += i * j

print(sum)