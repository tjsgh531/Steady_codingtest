import re

ex = input()

N = list(map(int, re.findall(r'\d+', ex)))
gi = re.findall(r'[^0-9]',ex)

isminus = False
cnt = 1
for i in gi:
    if i == '-':
        isminus = True
        break
    else:
        cnt +=1

if isminus:
    ans = sum(N[:cnt])-sum(N[cnt:])
else:
    ans = sum(N)
    
print(ans)    
