def solution(testlist):
    for test in testlist:
        a = test[0]
        b = test[1]
        aroute = []
        broute = []
        
        while a > 0:
            aroute.append(a)
            a = a//2
        
        while b > 0:
            broute.append(b)
            b = b//2
        result = max(set(aroute) & set(broute)) * 10
        print(result)

testCaseNum = int(input())
testlist = []

for _ in range(testCaseNum):
    testlist.append(list(map(int, input().split())))

solution(testlist)     
