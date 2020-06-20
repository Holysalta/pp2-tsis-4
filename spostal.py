def myfunc(n, k, stri):
    size = n+k+1
    sum=0
    if size != len(stri):
        return "No"
    if stri[n] != "-":
        return "No"
    for i in range (0,n):
        if stri[i]>="0" and stri[i]<="9":
            sum +=1 
    for i in range (n+1, size):
        if stri[i]>= "0" and stri[i]<="9":
            sum += 1
    if sum != size-1:
        return "No"
    else:
        return "Yes"
n , k =input().split()
n=int(n)
k=int(k)
stri=str(input())
print(myfunc(n,k,stri))

