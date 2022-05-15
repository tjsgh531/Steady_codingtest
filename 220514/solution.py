import copy

from sqlalchemy import false, true

def solution(cars):
    #1을 찾고
    #1에 인접한 0 다 1로 바꾸기
    
    #1옆에 4가 있으면 끝 
    #4가 없으면 4주변 0 다 4로 바꾸고
    #
    carsize = len(cars)
    for row in range(carsize):
        for col in range(carsize):
            item = cars[row][col]
            if item == 1:
                posx = row
                posy = col
    
    newcars = change(cars, posx, posy, carsize)
    if newcars[0] == 'find':
        return "find"

    for row in newcars:
        for item in row:
            print(item, end=' ')
        print()
    print()        


    return 0 

def change(cars, posX, posY, size):
    currentx = [(posX,posY)]
    findexit = False
    while not findexit:
        print(currentx)
        for pos in currentx:
            posx = pos[0]
            posy = pos[1]
            temp = []

            #down
            if posy+1 < size:
                if cars[posy+1][posx] == 0:
                    cars[posy+1][posx] = 1
                    temp.append((posx, posy+1))
                elif cars[posy+1][posx] == 4:
                    findexit = True
                    break    

            #up
            if posy-1 > 0:
                if cars[posy-1][posx] == 0:
                    cars[posy-1][posx] = 1
                    temp.append((posx, posy-1))
                elif cars[posy-1][posx] == 4:
                    findexit = True
                    break
            
            #right
            if posx+1 < size:
                if cars[posy][posx+1] == 0:
                    cars[posy][posx+1] = 1
                    temp.append((posx+1, posy))
                elif cars[posy][posx+1] == 4:
                    findexit = True
                    break

            if posx-1 > 0 :
                if cars[posy][posx-1] == 0:
                    cars[posy][posx-1] = 1
                    temp.append((posx-1, posy))
                elif cars[posy][posx-1] == 4:
                    findexit = True
                    break

        currentx = copy.deepcopy(temp)
        if len(currentx) == 0:
            break

    if findexit:
        return ["find"]
    else:
        return cars

print(solution([[0,0,3,0,0,0,0],[1,0,3,0,0,0,0],[0,0,3,0,0,0,0],[0,0,2,0,0,3,3],[2,2,2,0,2,0,0],[3,3,2,0,2,0,3],[3,3,2,0,2,0,4]]))
print(solution([[0,2,0,0,0],[0,4,2,0,0],[0,2,0,0,0],[0,0,0,2,1],[0,0,0,2,0]]))