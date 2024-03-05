import heapq

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    distance = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, current = heapq.heappop(pq)
        if current == end:
            return dist

        visited.add(current)

        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and (x, y) not in visited:
                new_dist = dist + 1
                if new_dist < distance[(x, y)]:
                    distance[(x, y)] = new_dist
                    heapq.heappush(pq, (new_dist, (x, y)))

    return -1  # No path found

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1]
]
start = (0, 0)  #ajdust accordingly both start and end value
end = (4, 4)
shortest_path_length = dijkstra(maze, start, end)
if shortest_path_length != -1:
    print(f"Shortest path length from {start} to {end}: {shortest_path_length}")
else:
    print("No path found")
