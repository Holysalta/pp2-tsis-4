def check(a,b,x,y):
    if (a<=x and b<=y) or (b<=x and a<=y):
        return "Thanks, Nurbek" 
    else:
        return "Impossible" 
a , b , x , y =map(int,input().split())
print(check(a,b,x,y))

    