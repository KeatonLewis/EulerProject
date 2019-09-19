def Collatz(start):
    sequence = [start]
    while sequence[-1] > 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    return len(sequence) - 1

maxLength = 1
startValue = 1
for i in range(1, 1000000, 2):
    current = Collatz(i)
    if  current > maxLength:
        maxLength = current
        startValue = i

print(startValue)

# There is a much faster solution here where you us a hash table 
# Essentially you just check after every step in the Collatz sequence if you've done this number before
# Then you know how many steps left to the end and you just add that to the current number of steps
# I could not get that to work quickly however and it's late 