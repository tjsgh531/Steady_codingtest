def solution(answers):
    one = [1, 2, 3, 4, 5] * (10000//5)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (10000//8)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000//10)

    scores = [0, 0, 0]
    for idx, value in enumerate(answers):
        if one[idx] == value:
            scores[0] += 1
        if two[idx] == value:
            scores[1] += 1
        if three[idx] == value:
            scores[2] += 1
            
    max_score = max(scores)
    answer = []
    for idx, value in enumerate(scores):
        if value == max_score:
            answer.append(idx+1)
    return answer