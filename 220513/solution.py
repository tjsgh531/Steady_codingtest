from dataclasses import dataclass


class Node:
    def __init__(this, index, data, next = None, pre = None):
        this.index = index
        this.data = data
        this.next = next
        this.pre = pre

def makeLinkedList(numlist):
    head = None
    for idx, item in enumerate(numlist):
        newnode = Node(idx+1, item)
        currentnode = head
        if head:
            while currentnode.next:
                currentnode = currentnode.next
            currentnode.next = newnode
            newnode.pre = currentnode
        else: #head가 없는 경우
            head = newnode
    currentnode.next.next = head #마지막 노드 head로 연결
    head.pre = currentnode.next #head pre를 마지막 노드로 연결

    return head

def solution(num, numlist):
    head = makeLinkedList(numlist)
    result = []

    curnode = head
    for i in range(num):
        #print(f"pre : {curnode.pre.index}\t index: {curnode.index}\t next:{curnode.next.index}")
        #curnode = curnode.next
        result.append(curnode.index)
        curnode.pre.next = curnode.next
        curnode.next.pre = curnode.pre

        repeatnum = curnode.data
        if repeatnum < 0:
            for j in range(-repeatnum):
                curnode = curnode.pre
        else:
            for j in range(repeatnum):
                curnode = curnode.next
    return result

print(solution(5, [3, 2, 1, -3, -1]))    