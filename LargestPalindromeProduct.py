n1 = 100
n2 = 100
palindromes = []

def isPalindrome(n):
    temp = [int(num) for num in str(n)]
    i = 0
    while i < len(temp) - 1:
        if temp[i] != temp[-i - 1]:
            return False
        i += 1
        
    return True
    

while n1 < 1000:
    while n2 < 1000:
        if isPalindrome(n1 * n2):
            palindromes.append(n1 * n2)
        n2 += 1
    n2 = 100
    n1 += 1

print(max(palindromes))