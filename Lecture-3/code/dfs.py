# representing graph using adjaceny list (python dictionary)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

# initializing visisted array
visited = [False for x in range(len(graph))]

def dfs(v):
    # runs for every vertex. This is because the condition in the loop
    # ensures that this line is not repeated for a vertex.
    visited[v] = True
    # visiting node. printing vertex
    print(v, end=" ")

    # runs for every edge
    for child in graph[v]:
        if not visited[child]:
            dfs(child)

    # Time complexity: O(V+E)

def fast_dfs(v):
    if visited[v]:
        return None

    visited[v] = True
    # visiting node. printing vertex
    print(v, end=" ")

    for child in graph[v]:
        return dfs(child)


# running dfs, starting from vertex 0
print("Using normal dfs: ", end=" ")
dfs(0)

# printing new line
print() 

# reinitializing visisted array
visited = [False for x in range(len(graph))]

# running fast dfs, starting from vertex 0
print("Using fast dfs: ", end=" ")
fast_dfs(0)
