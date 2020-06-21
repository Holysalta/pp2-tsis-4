def a2(s):
    if len(s)==0:
        return False
    result=True
    for c in s:
        k=ord(c)
        if k < 97 or k>122:
            result= False
            break
    return result
def a3(s):
    position1=s.find("@")
    position2=s.find(".")
    return position1 < position2
def a1(s,t):
    result = 0
    for c in s:
        if c==t: 
            result=result+1
    return result==1

def solution(s):
    result="No"
    if a1(s,'@') and a1(s,'.') and a3(s):
        parts=s.split('@')
        aaa=parts[0]
        part2=parts[1].split('.')
        bbb=part2[0]
        ccc=part2[1]
        if a2(aaa) and a2(bbb) and a2(ccc):
            result="Yes"
    return result
print(solution(input()))