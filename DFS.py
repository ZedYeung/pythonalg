def dfs_topsort(G):
    visited,result=set(),[]
    def recurse(u):
        if u in visited:
            return
        visited.add(u)
        for v in G[u]:
            recurse(v)
        result.append(u)
        for u in G:
            recurse(u)
        result.reverse()
        return result

N={'a':set('bcdef'),
   'b':set('ce'),
   'c':set('d'),
   'd':set('e'),
   'e':set('f'),
   'f':set('cgh'),
   'g':set('fh'),
   'h':set('fg')}