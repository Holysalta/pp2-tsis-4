def numberToBase(n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % 7))
        n //= 7
    return digits[::-1]

number=int(input())
for i in numberToBase(number):
    print(i,end='')
