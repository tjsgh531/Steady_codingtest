def solution(node_num, ducks):
    init_tree = [None] + [ 0 for _ in range(node_num)]

    for item in ducks:
        currentitem = item
        resultval = 0
        while currentitem > 0:
            if init_tree[currentitem] != 0:
                resultval = init_tree[currentitem]
            currentitem = currentitem // 2
        
        if resultval == 0:
            init_tree[item] = item
        
        print(resultval)

inputvalue = input().split(' ')
nodeNum = int(inputvalue[0])
duckNum = int(inputvalue[1])
ducks = []

for _  in range(duckNum):
    item = int(input())
    ducks.append(item)

solution(nodeNum, ducks)

