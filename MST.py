import heapq

def prim_mst(graph):
    n = len(graph)
    min_spanning_tree = []
    visited = set()
    start_vertex = 0
    visited.add(start_vertex)
    edges = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            min_spanning_tree.append((u, v, weight))
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))

    return min_spanning_tree

# Example usage:
graph = {
    0: [(1, 2), (2, 1), (3, 4)],
    1: [(0, 2), (3, 2)],
    2: [(0, 1), (3, 5)],
    3: [(1, 2), (2, 5)]
}

minimum_spanning_tree = prim_mst(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
