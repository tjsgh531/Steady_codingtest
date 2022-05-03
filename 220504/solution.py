from collections import deque

from defusedxml import DTDForbidden

def solution(total, selectarr):
    totalnum = total

    change_num = 0
    result = 0;

    for num in selectarr:
        print(f"num : {num}", end='\t')
        print(f"total num : {totalnum}", end='\t')
        change_num = change_num % totalnum
        print(f"change num : {change_num}", end='\t')
        
        currentnum = num+change_num
        if currentnum < 0 :
            currentnum = totalnum + change_num + num
        currentnum = currentnum % totalnum
        print(f"current num : {currentnum}", end='\t')

        rot = totalnum-currentnum+1
        reverserot = currentnum -1
        print(f"rot num : {rot}", end='\t')
        print(f"reverserot num : {reverserot}", end='\t')
        
        if rot >= reverserot :
            result += reverserot
            change_num -= (reverserot+1)
            
        else:
            result += rot
            change_num += (rot -1)
        print(f"result : {result}", end='\n')
        totalnum -= 1
    return result

print(solution(32, [27, 16, 30, 11, 6, 23]))