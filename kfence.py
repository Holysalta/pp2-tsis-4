n , k = map(int,input().split())
matrix = []
for i in range (n):
    num = list(map(int,input().split()))
    matrix.append(num)
x = False
for i in range(n):
    summa = 0
    for j in range(3):
        summa += matrix[i][j]
    if summa // 3 >= k:
        x = True
if x:
    print("YES")
else:
    print("NO")

