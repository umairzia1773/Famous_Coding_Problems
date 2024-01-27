'''1st method'''

# def has_eulerian_path(graph, node, visited, count):
#     visited[node] = True
#     count[0] += 1


#     for neighbor in graph[node]:
#         if not visited[neighbor]:

#             if has_eulerian_path(graph, neighbor, visited, count):
#                 return True


#     return count[0] == len(graph)


# graph = {
#     "A": ["B", "C", "D"],
#     "B": ["A", "C", "D"],
#     "C": ["A", "B", "D"],
#     "D": ["A", "B", "C"]
# }


# visited = {node: False for node in graph}
# count = [0]


# start_node = "D"


# if has_eulerian_path(graph, start_node, visited, count) and count[0] == len(graph):
#     print("An Eulerian Path Exists")
# else:
#     print("No Eulerian Path Exists")





'''2nd method'''

# def is_konigsberg_solvable(adj_matrix):
#     def dfs(node):
#         nonlocal count
#         visited[node] = True
#         count += 1
#         for neighbor in range(len(adj_matrix)):
#             if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
#                 dfs(neighbor)

#     num_nodes = len(adj_matrix)
#     visited = [False] * num_nodes
#     count = 0


#     dfs(0)


#     if count == num_nodes and all(sum(row) % 2 == 0 for row in adj_matrix):
#         return True
#     else:
#         return False


# solvable_adjacency_matrix = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [0, 1, 1, 0]
# ]

# if is_konigsberg_solvable(solvable_adjacency_matrix):
#     print("There exists a path in the City of Königsberg that crosses each bridge exactly once.")
# else:
#     print("There is no path in the City of Königsberg that crosses each bridge exactly once.")
