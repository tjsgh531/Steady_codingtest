def solution(array, commands):
    answer = []
    for order in commands:
        i = order[0]
        j = order[1]
        k = order[2]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer