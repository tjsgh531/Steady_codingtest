def solution(data , n, cnt):
    if len(data) > 1:
        newdata =[]
        tempdata = []
        if n % 2 == 0:
            for i in data:
                tempdata.append(i)
                if len(tempdata) == 2:
                    newitem = sum(tempdata)
                    newdata.append(newitem)
                    cnt += newitem
                    tempdata.clear()
            return solution(data, len(data), cnt)
        else:
            maxval = max(data)
            for i in data:
                if i == maxval:
                    newdata.append(i)
                else:
                    tempdata.append(i)
                    if len(tempdata) == 2:
                        newdata.append(sum(tempdata))
                        tempdata.clear()
            return solution(newdata, len(newdata), cnt)

    else:
        return cnt
T = int(input())
for i in range(T):
    N = int(input())
    data = list(map(int, input().split()))
