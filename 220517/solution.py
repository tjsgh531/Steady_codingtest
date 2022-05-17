import heapq
from inspect import stack

class Node:
    def __init__(self, nodenum, data, left =None, right=None):
        self.nodenum = nodenum
        self.data = data
        self.left = left
        self.right = right
            
def solution(nodeinfo):
    templist = []

    count = 0
    for node in nodeinfo:
        count +=1
        #newnode(-y, x, nodenum)
        newitem = [-node[1], node[0], count]
        heapq.heappush(templist, newitem)

    head = None
    while templist:
        item = heapq.heappop(templist)
        newnode = Node(item[2], item[1])
        if head:
            currentnode = head
            while currentnode:
                if currentnode.data > newnode.data:
                    if currentnode.left:    
                        currentnode = currentnode.left
                    else:
                        currentnode.left = newnode
                        break
                else:
                    if currentnode.right:
                        currentnode = currentnode.right
                    else:
                        currentnode.right = newnode
                        break
        else:
            head = newnode
    postorder(head)

#후위 순회
def postorder(root):
    if root.left != None:
        postorder(root.left)
    if root.right != None:
        postorder(root.right)
    print(root.nodenum)

#전위 순회
def preorder(root):
    print(root.nodenum)
    if root.left != None:
        postorder(root.left)
    if root.right != None:
        postorder(root.right)


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])