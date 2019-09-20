# Again this is too easy in Python without int size limits

power = 2 ** 1000

print(sum([int(digit) for digit in str(power)]))