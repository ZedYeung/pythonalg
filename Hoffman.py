from heapq import heappop,heappush,heapify
from itertools import count
def huffman(seq, frq):
    num=count()
    trees=list(zip(frq,num,seq))
    heapify(trees)
    while len(trees)>1:
        frqa,_,a=heappop(trees)
        frqb,_,b=heappop(trees)
        n=next(num)
        heappush(trees,(frqa+frqb,n,[a,b]))
    return trees[0][-1]

huffman(seq,frq)
seq="abcdefghi"
frq=list(range(4,13))