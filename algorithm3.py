import math
from itertools import permutations


# O(n!)
def travelling_salesman_problem(graph, s):
    vertex = []
    for i in range(4):
        if i != s:
            vertex.append(i)

    min_path = math.inf
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)

    return min_path

