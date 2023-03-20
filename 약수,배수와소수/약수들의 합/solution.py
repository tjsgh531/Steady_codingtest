while(1):
    n = int(input())
    if n == -1:
        break

    measures = []
    for i in range(1, n):
        if n % i == 0:
            measures.append(i)
    
    print(sum(measures))
    
    if n == sum(measures):
        temp = " + ".join(list(map(chr, measures)))
        print(temp)
        print(f"{n} = {temp}" )
    else:
        print(f"{n} = is NOT perfect.")