def favnum(n):
    sum = 0
    for digit in str(n):
     sum += int(digit)
    lastdig = n % 10
    if sum % lastdig == 0:
        return "Yes"
    else:
        return "No"
n = int(input())
print(favnum(n))