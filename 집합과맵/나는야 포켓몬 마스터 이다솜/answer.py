n, m = map(int, input().split()) # n: 포켓몬 개수, m: 문제 개수

# 포켓몬 이름과 번호를 매핑하는 딕셔너리 생성
name_to_num = {}
num_to_name = {}
for i in range(1, n+1):
    name = input()
    name_to_num[name] = i
    num_to_name[i] = name

# 문제 해결
for i in range(m):
    q = input()
    if q.isdigit(): # 입력이 번호일 경우
        print(num_to_name[int(q)])
    else: # 입력이 이름일 경우
        print(name_to_num[q])
