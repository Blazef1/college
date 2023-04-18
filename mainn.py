inc = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}

visited = set()
Q = []
BFS = []

def bfs(v):
    if v in visited:
        return
    visited.add(v)
    BFS.append(v)
    for i in inc[v]:
        if not i in visited:
            Q.append(i)
    while Q:
        bfs(Q.pop(0))

start = 1
bfs(start)
print(BFS)