# 설마 
import sys

input = sys.stdin.readline

sen = []
while 1:
    temp = input()
    if temp =='.':
        break
    else:
        sen.append(temp)

for sentence in sen:
    small_stack = 0
    big_stack = 0
    for word in sentence:
        if word == '(':
            small_stack += 1
        elif word == ')':
            small_stack -= 1
            if small_stack < 0:
                print("no")
                break
        elif word == '[':
            big_stack += 1
        elif word == ']':
            big_stack -= 1
            if big_stack < 0:
                print("no")
                break
    else:
        if small_stack == 0 and big_stack == 0:
            print("yes")
        else:
            print("no")