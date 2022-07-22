def solution(answers):
    length = len(answers)
    one = [ i % 5 + 1 for i in range(length)]
    one_sc = 0
    for item, ans in zip(one, answers):
        if item == ans:
            one_sc +=1
    
    two_sc = 0
    cnt = 1
    for item, ans in zip(range(length), answers):
        if item % 2 == 0: 
            if ans == 2:
                two_sc += 1
        else:
            if cnt == 2:
                cnt+=1
            if cnt == ans:
                two_sc +=1
            cnt += 1
    
    three_sc = 0
    temp = [3,1,2,4,5]
    for i, ans in zip(range(length), answers):
        idx = (i%6)//2
        if temp[idx] == ans:
            three_sc += 1

    print(one_sc, two_sc, three_sc)
    max_score = max(one_sc, two_sc, three_sc)
    answer = []
    if one_sc == max_score:
        answer.append(1)
    if two_sc == max_score:
        answer.append(2)
    if three_sc == max_score:
        answer.append(3)

    return answer

print(solution([1,2,3,4,5]))