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
                    mycar.append((row, col))
                    findcar = true
                    break
    #go trip
    for pos in mycar:
        newrow = [pos[0]-1, pos[0]+1]
        newcol = [pos[1]-1, pos[1]+1]
        
        #board 밖으로 나가는 예외 처리
        for i in newrow:
            if i < 0 or i == len(cars):
                newrow.remove(i)
        for j in newcol:
            if j < 0 or  j == len(cars):
                newcol.remove(j)
        
        if len(newrow) + len(newcol) == 0:
            continue
        
        print(f"newrow : {newrow}")
        print(f"newcol : {newcol}")
        # UP & DOWN
        for rowitem in newrow:
            newpos = cars[rowitem][pos[1]]
            if newpos == 0:
                cars[rowitem][pos[1]] = 1
                mycar.append((rowitem,pos[1]))
            # 2 여도 일단 못 지나 간다고 해야 겠지?
            elif newpos == 4:
                return 0
        
        # RIGHT & LEFT      
        for colitem in newcol:
            newpos = cars[pos[0]][colitem]
            if newpos == 0:
                cars[pos[0]][colitem] = 1
                mycar.append((pos[0],colitem))
            # 2 여도 일단 못 지나 간다고 해야 겠지?
            elif newpos == 4:
                return 0

        
print(solution([[0,2,0,0,0],[0,4,2,0,0],[0,2,0,0,0],[0,0,0,2,1],[0,0,0,2,0]]))
                    
                    