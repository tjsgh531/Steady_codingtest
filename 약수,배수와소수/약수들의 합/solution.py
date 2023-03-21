while(1):
    n = int(input())
    if n == -1:
        break

    measures = []
    for i in range(1, n):
        if n % i == 0:
            measures.append(i)
    
    if n == sum(measures):
        temp = " + ".join(list(map(str, measures)))
        print(f"{n} = {temp}" )
    else:
        print(f"{n} is NOT perfect.")
