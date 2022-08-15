from collections import Counter

def solution(N, stages):
    stagesnum = dict(Counter(stages));
    print(stagesnum)


    stage_reach = [0] * (N+2)

    for i in stagesnum:
        stage_reach[i] = stagesnum[i]
    
    wrong = []
    alive = len(stages)

    # 리스트
    # 튜플
    # 딕셔너리
    stage_reach = [0, 1, 3, 2, 1, 0, 1]
    for i in range(1, N+1):
        wrong.append((stage_reach[i] / alive, i))
        alive -= stage_reach[i]

    print(wrong)
    print(sorted(wrong, reverse=True))
    
    return 0

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])