def has_eulerian_path(graph):
    for node in graph:
        visited = {node: False for node in graph}
        count = [0]
        if has_path_from_node(graph, node, visited, count) and count[0] == len(graph):
            return True, node
    return False, None

def has_path_from_node(graph, node, visited, count):
    visited[node] = True
    count[0] += 1

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_path_from_node(graph, neighbor, visited, count):
                return True

    return count[0] == len(graph)

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["A", "B", "C"]
}

exists, start_node = has_eulerian_path(graph)

if exists:
    print("An Eulerian Path Exists in the graph, starting from node", start_node)
else:
    print("No Eulerian Path Exists in the graph")
