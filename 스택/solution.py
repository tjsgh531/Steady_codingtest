N = int(input())
orders = []

for _ in range(N):
    input_order = list(input().split())
    orders.append(input_order)

stack = []
for o in orders:
    order = o[0]
    if order == 'push':
        item = int(o[1])
        stack.append(item)
    
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            item = stack.pop()
            print(item)

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
