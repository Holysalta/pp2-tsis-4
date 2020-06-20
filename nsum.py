def sumnum (n,m):
    sum = 0
    if n == 0:
        return m
    elif m ==0:
        return n
    else:
        dig1 = n% 10
        dig2 = m % 10
        sumof= (n - dig1)+(m-dig2)
        sum=sumof +dig1 +dig2
        return sum
n , m =map(int,input().split())
print(sumnum(n,m))
