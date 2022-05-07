def solution(arr, step):
    result = []
    temp = []

    for i in arr:
        if i > 0:
            if len(temp) == 0:
                result.append(i)
            else:
                if len(result) == 0:
                    result.append(i)
                    temp.clear()
                else:# -부분 어캐하지
                    length = len(temp);
                    
                    

        else:
            temp.append(i)