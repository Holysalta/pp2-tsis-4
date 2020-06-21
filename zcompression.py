def check(string, n): 
      a = 0
      for i in range(0, n): 
            for j in range(0, i + 1):
                if (string[i] == string[j]): 
                      break
            if (j == i):
                      string[a] = string[i] 
                      a += 1             
      return "".join(string[:a])  
string= str(input())
n = len(string) 
print(check(list(string), n)) 
  




