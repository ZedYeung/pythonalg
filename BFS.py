from collections import deque
def bfs(G,s):
    pre, queue = {s:None}, deque([s])
    while queue:
        u=queue.popleft()
        for v in G[u]:
            if v in pre:
                continue
            queue.append(v)
            pre[v]=u
    return pre







