def solution(arr, size):
    result = []
    copyarr = arr
    current_idx = 0

    #처음 시작 지점 찾기
    for idx, item in enumerate(arr):
        if item > 0:
            current_idx = idx
            result.append(item)
            break
    else:
        return min(arr)
    
    while current_idx < len(arr):
        selectlist = copyarr[current_idx:current_idx+size+1]
        for idx, item in enumerate(selectlist) :
            if item > 0:
                current_idx += idx+1
                result.append(item)
            else:
                #보폭 내에 -밖에 없는 경우 멈출지 손해 감수하고 건널지 결정 해야하네...
                #이득을 묶음 단위로 묶어야 겠다 - 힘들듯...
                #양수가 붙어 있으면 합한 숫자로 
                # 양수 - 음 음 음 ... - 양수 - 음 음 ... - 양수 로 가공 가능
                