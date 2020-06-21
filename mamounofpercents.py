
num = list(map(int, input().split()))
even = 0
odd = 0
for i in range(0,len(num)):
    if num[i]>=0 and num[i]%2 == 0:
        even += 1
    elif num[i]>=0 and num[i]%2 == 1:
        odd += 1
    else:
        break
result1 = even*100/(len(num)-1)
result2=odd*100/(len(num)-1)

if (result1*10)%10==0 and (result2*10)%10==0:
    result1=int(result1)
    result2=int(result2)
else:
    result1=round(result1,4)
    result2=round(result2,4)
result1=str(result1)
result2=str(result2)
print(result1+"%",result2+"%")

        


   