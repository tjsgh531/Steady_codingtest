def solution(node_num, ducks):
    init_tree = [None] + [ 0 for _ in range(node_num)]
    result = []
    for item in ducks:
        temp = []
        currentitem = item
        while currentitem > 0:
            temp.append(currentitem)
            currentitem = currentitem // 2

        for _ in range(len(temp)):
            current_node = temp.pop()
            if init_tree[current_node] != 0:
                result.append(init_tree[current_node])
                break
        else:
            init_tree[item] = item
            result.append(0)

    for val in result:
        print(val)

inputvalue = input().split(' ')
nodeNum = int(inputvalue[0])
duckNum = int(inputvalue[1])
ducks = []

for _  in range(duckNum):
    item = int(input())
    ducks.append(item)

solution(nodeNum, ducks)
