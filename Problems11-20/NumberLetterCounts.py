nums = {1 : "one", 2: "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven",
        8: "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 
        14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 
        19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty",
        70 : "seventy", 80 : "eighty", 90 : "ninety", 0 : ""}

sum = 0
for i in range(1, 1001):
    currentNum = [int(digit) for digit in str(i)]
    if i <= 20:
        sum += len(nums[i])
    elif i < 100:
        sum += len(nums[currentNum[0]*10] + nums[currentNum[1]])
    elif i < 1000:
        if currentNum[1] == 0 and currentNum[2] == 0:
            sum += len(nums[currentNum[0]] + "hundred")
        elif currentNum[1]*10 + currentNum[2] <= 20:
            sum += len(nums[currentNum[0]] + "hundredand" + nums[currentNum[1]*10 + currentNum[2]])
        else:
            sum += len(nums[currentNum[0]] + "hundredand" + nums[currentNum[1]*10] + nums[currentNum[2]])
    else:
        sum += len("onethousand")

print(sum)