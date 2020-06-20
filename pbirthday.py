def inBox(x,y,a,b,pos1,pos2):
    if (pos1<a and pos1>=x and pos2>=b and pos2 <=y ):
        print("yes")
        return
    
    print("no")
x,y,a,b,pos1,pos2 = map(int,input().split())
inBox(x,y,a,b,pos1,pos2)
