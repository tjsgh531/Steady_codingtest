class Node:
    def __init__(self, data, next=None, pre=None):
        self.data = data
        self.next = next
        self.pre = pre

def makeLinkedList(N):
    for i in range(N):
        newnode = Node(i+1)
        if i == 0:
            head = newnode
        else:
            currentNode = head
            while currentNode.next:
                currentNode.next.pre = currentNode
                currentNode = currentNode.next
            currentNode.next = newnode
            currentNode.next.pre = currentNode
            
    currentNode.next.next = head
    head.pre = currentNode.next
    return head

def solution(N, K):
    head = makeLinkedList(N)
    result = []
    
    for j in range(N):
        for i in range(K):
            head = head.next

        selecteNode = head.pre
        result.append(selecteNode.data)
        head.pre = selecteNode.pre
        selecteNode.pre.next = head
    
    resultstr = "<"+', '.join(map(str, result))+">"
    print(resultstr)

            
solution(7,3)
