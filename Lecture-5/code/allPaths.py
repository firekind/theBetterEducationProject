# problem is to find all the paths from a
# source vertex to a destination vertex
# in a directed graph

adjList = {
    0: [1, 3],
    1: [2, 3],
    2: [5],
    3: [4, 3], # cycle here
    4: [5],
    5: []
}

visited = [False for _ in range(len(adjList))]
walk = []
path = []

def dfs(v, dest):
    # marking vertex as visited
    visited[v] = True

    # appending the vertex to the current walk
    walk.append(v)

    # if the destination has been reached, append 
    # the current walk to the path
    if v == dest:
        path.append(list(walk))

    # else, dfs
    else:
        for adjacentVertex in adjList[v]:
            if not visited[adjacentVertex]:
                dfs(adjacentVertex, dest)
    
    # remove the vertex from the current walk,
    # as this vertex may not be part of the path
    # to the destination
    walk.pop()

    # set visited to False so that this vertex
    # can be visited again. This is so that there
    # is a possibility that another path may exist
    # to the destination through this vertex
    visited[v] = False
    

if __name__ == "__main__":
    dfs(0, 5)
    print(path)
 