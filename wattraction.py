def check(n,num,height):
    x=0
    for k in range(n):
        num.append(k)
        for i in range(len(num)):
            if num[i]>=height:
                x +=1
        return x

n=int(input())
num=list(map(int,input().split()))
height=int(input())

print(check(n,num,height))

    
        

