# O(n^3)
def create_cube_matrix(n):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append([])
            for q in range(0, n):
                matrix[i][j].append(0)
    return matrix
