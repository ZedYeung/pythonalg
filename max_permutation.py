def max_permutation(M):
    n=len(M)
    max=set(range(n))
    count=[0]*n
    for i in M:
        count[i]+=1
    useless=[i for i in max if count[i]==0]
    while useless:
        i=useless.pop()
        max.remove(i)
        chair=M[i]
        count[chair]-=1
        if count[chair]==0:
            useless.append(chair)
    return max

M=[2,2,0,5,3,5,7,4]
max_permutation(M)
