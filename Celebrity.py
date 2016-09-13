from random import randrange
def celebrity(G):
    'solve the celebrity problem'
    n=len(G)
    u, v = 0, 1
    for celeb in range(2,n+1):
        if G[u][v]: u=celeb
        else:   v=celeb
    if u==n:    celeb=v
    else:   celeb=u
    for w in range(n):
        if celeb == w:
            continue
        if G[c][w]:
            break
        if not G[w][c]:
            break
    else:
        return celeb
    return None
n=100
G=[[randrange(2) for i in range(n)] for i in range(n)]
c=randrange(n)
for i in range(n):
    G[i][c] = True
    G[c][i] = False
celebrity(G)
