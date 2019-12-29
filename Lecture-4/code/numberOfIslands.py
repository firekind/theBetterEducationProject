# Problem is to find the number of islands
# given: 
# [ 1, 0, 0, 0, 1,
#   0, 1, 0, 0, 1,
#   0, 1, 0, 1, 0
#   0, 1, 1, 0, 0,
#   1, 1, 1, 0, 0 ]
# A '1' represents land, '0' represents sea.
# the number of islands is 4 as an island
# is a slice of the matrix that has all elements
# as 1. However, 
# [0, 1
#  1, 0]
# has two islands, not 1. Thus, diagonals are not
# connected.
# This problem essentially counts the number of clusters
# of 1's in the matrix.
# worst case time complexity is O(n^2), as each element 
# of the matrix should be traversed, and the time complexity 
# of dfs is O(V+E), which is not as worse as O(n^2)

mat = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0]
]

def dfs(i, j, mat, visited):
    """
    Applies Depth first search.
    
    Args:
        i (int): The row index of the src element
        j (int): The column index of the src element
        mat (List[List[int]]): The input matrix
        visited (List[List[bool]]): The visited matrx
    """
    if visited[i][j]:
        return None

    visited[i][j] = True

    # Checking the adjacent vertices whether they 
    # are land masses
    # left
    if j - 1 >= 0 and not visited[i][j-1] and mat[i][j-1] == 1:
        dfs(i, j-1, mat, visited)
    # right
    if j + 1 < len(mat[0]) and not visited[i][j+1] and mat[i][j+1] == 1:
        dfs(i, j+1, mat, visited)
    # top
    if i - 1 >= 0 and not visited[i-1][j] and mat[i-1][j] == 1:
        dfs(i-1, j, mat, visited)
    # bottom
    if i + 1 < len(mat) and not visited[i + 1][j] and mat[i+1][j] == 1:
        dfs(i+1, j, mat, visited)

    return None
    

def numberOfIslands(mat):
    """
    Counts the number of islands given the matrix
    
    Args:
        mat (List[List[int]]): The matrix
    
    Returns:
        int: The number of islands
    """

    count = 0

    # creating 2D visited array
    visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]

    # going through every element in `mat`
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # if `mat` is land and its not visited, 
            # apply dfs
            if mat[i][j] != 0 and not visited[i][j]:
                dfs(i, j, mat, visited)
                count += 1
    
    return count

print(numberOfIslands(mat))
