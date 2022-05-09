def solution(n, spinlist):
    result = [None] * n
    currentidx = 0
    for item in spinlist:
        num = item[0]
        en = item[1]
        currentidx = (currentidx+num)%n
        
        if result[currentidx]:
            if en == result[currentidx]:
                continue
            else:#들어있는것이 지금 알파벳 과 다른경우
                return ["!"]
        
        else:#아무것도 안들어 있을 경우
            result[currentidx] = en
    
    returnlist = []
    for i in range(n):
        idx = currentidx -i
        item = result[idx]
        if item == None:
            returnlist.append("?")
        else:
            returnlist.append(item)
    return returnlist

print(solution(5,[(1,'A'),(2,'B'),(5, 'B'),(1, 'C'),(2, 'A'),(2, 'B')]))
print(solution(3,[(1, 'A'),(2, 'B'), (3, 'C')]))
print(solution(8,[(4,'V'),(3, 'I'), (7,'T'),(7,'A'),(6,'R'),(5,'N'),(1,'O'),(9,'H')]))