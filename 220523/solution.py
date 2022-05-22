def solution(numlist):
    sortedlist = [numlist[0]]

    for item in numlist:
        if sortedlist[-1] > item:
            sortedlist.pop()
            sortedlist.append(item)
        elif sortedlist[-1] < item:
            sortedlist.append(item)
    print(len(sortedlist))                    

repeatnum = int(input())
numlist = list(map(int, input().split(' ')))
solution(numlist)