import re

def solution(new_id):
    #1
    new_id1 = new_id.lower()
    print(new_id1)
    #2
    new_id2 = re.sub( '[^a-z0-9._-]', '', new_id1)
    print(new_id2)
    #3
    new_id3 = re.sub('[.]+', '.', new_id2)
    print(new_id3)
    #4
    new_id4 = re.sub('^[.]|[.]$', '', new_id3 )
    print(new_id4)
    #5
    if len(new_id4) <= 0 : 
        new_id4 = "a"
        print(new_id4)
    #6
    if len(new_id4) >= 16 :
        new_id4 = new_id4[:15]
        while new_id4[-1] == ".":
            new_id4 = re.sub('[.]$', '', new_id4)
        print(new_id4)
    #7
    while len(new_id4) <= 2:
        new_id4 = new_id4 + new_id4[-1]
        print(new_id4)
    
    return new_id4

print(solution("123_.def"))