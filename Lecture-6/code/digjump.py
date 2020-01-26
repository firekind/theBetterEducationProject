from typing import Dict, List
from collections import defaultdict

# s = "012134444444443"
s = "01234567890"


trim = lambda s: s[:s.index(s[-1]) + 1]

def constructAdjList(s: str) -> Dict[str, List[str]]:
    adjList: Dict[str, List[str]] = {}

    # constructing the keys for the adjaceny list
    for key in range(len(s)):
        adjList[key] = []

    for i in range(len(s)):
        if i != 0:
            adjList[i].append(i - 1)

        if i != len(s) - 1:
            adjList[i].append(i + 1)

        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                adjList[i].append(j)
    
    return adjList


def bfs(adjList: Dict[str, List[str]], dest: int) -> None:
    visited = [False for i in range(len(adjList))]
    visited[0] = True
    q = [0]
    path = defaultdict(lambda: float('inf'))
    path[0] = 0

    while q:
        v = q.pop(0)

        for adjacentVertex in adjList[v]:
            if not visited[adjacentVertex]:
                visited[adjacentVertex] = True
                q.append(adjacentVertex)
                path[adjacentVertex] = path[v] + 1

    return path[dest] + 1


trimmed_s = trim(s)
adjList = constructAdjList(trimmed_s)
print(bfs(adjList, len(trimmed_s) - 1))
