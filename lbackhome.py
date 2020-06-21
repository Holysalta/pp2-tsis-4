def isBack(path):
    x = 0
    y = 0 
    while True:
        for i in range (0,len(path)):
            if path[i] == "R":
                x += 1
            elif path[i] == "L":
                x -= 1
            elif path[i] == "U":
                y += 1
            elif path[i] == "D":
                y -= 1
            else:
                return "mistake"
        return (x == 0 and y ==0)

path = input()
print(isBack(path))
    
            
            