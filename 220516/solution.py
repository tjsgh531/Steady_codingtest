from collections import deque


def solution(cars):
    #find my car
    findcar = False
    mycar = []
    for row in range(len(cars)):
        if findcar:
            break
        else:
            for col in range(len(cars)):
                if cars[row][col] == 1:
                    mycar.append((row, col, 0))
                    findcar = True
                    break
    #go trip
    currentcost = 0
    prelen = 0
    pos = None
    while True:
        print(currentcost)
        if len(mycar) == 0:
            break
        
        #이전 위치
        if pos != None:
            prepos = pos

        pos = mycar.pop()
        currentcost += pos[2]
        
        #다시 돌아 갔다면
        if len(mycar) < prelen:
            #돌아간 곳이 2이면 currentcost 줄이기
            if prepos[2] == 1:
                currentcost -= 1    
        else:
            prelen = len(mycar)

        print(f"mycar :{mycar} \t pos :{pos}  ")
        newrow = [pos[0]-1, pos[0]+1]
        newcol = [pos[1]-1, pos[1]+1]
        
        #board 밖으로 나가는 예외 처리
        for i in newrow:
            if i < 0 or i == len(cars):
                newrow.remove(i)
        for j in newcol:
            if j < 0 or  j == len(cars):
                newcol.remove(j)
        
        #길없음
        if len(newrow) + len(newcol) == 0:
            continue

        temp =deque()
        # UP & DOWN
        for rowitem in newrow:
            newpos = cars[rowitem][pos[1]]
            if newpos == 0:
                cars[rowitem][pos[1]] = 1
                temp.append((rowitem,pos[1],0))
            elif newpos == 2:
                cars[pos[0]][colitem] = 1
                temp.appendleft((rowitem,pos[1],1))
            elif newpos == 4:
                return currentcost
        
        # RIGHT & LEFT      
        for colitem in newcol:
            newpos = cars[pos[0]][colitem]
            if newpos == 0:
                cars[pos[0]][colitem] = 1
                temp.append((pos[0],colitem,0))
            elif newpos == 2:
                cars[pos[0]][colitem] = 1
                temp.appendleft((pos[0],colitem,1))
            elif newpos == 4:
                return currentcost
        mycar = mycar + list(temp)

        
#print(solution([[0,2,0,0,0],[0,4,2,0,0],[0,2,0,0,0],[0,0,0,2,1],[0,0,0,2,0]]))
print(solution([[0,0,3,0,0,0,0,],[1,0,3,0,0,0,0],[0,0,3,0,0,0,0,],[0,0,2,0,0,3,3],[2,2,2,0,2,0,0],[3,3,2,0,2,0,3],[3,3,2,0,2,0,4]]))
                    