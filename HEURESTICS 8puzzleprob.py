import heapq

class eight_Puzzle:
    def __init__(self, state, parent=None, action=None, g=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = self.Manhatten_Distance()
        self.f = self.g + self.h

    def Manhatten_Distance(self):
        h = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j] - 1, 3)
                    h += abs(x - i) + abs(y - j)
        return h

    def __lt__(self, other):
        return self.f < other.f

def get_position(node):
    neighbors = []
    state = node.state
    empty_tile = None

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_tile = (i, j)
                break

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in moves:
        ni, nj = empty_tile[0] + dx, empty_tile[1] + dy
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[empty_tile[0]][empty_tile[1]], new_state[ni][nj] = new_state[ni][nj], new_state[empty_tile[0]][empty_tile[1]]
            neighbors.append(eight_Puzzle(new_state, node, (ni, nj)))

    return neighbors

def IDS_Search(initial_state):
    max_depth = 0
    while True:
        result = depth_limited_search(initial_state, max_depth)
        if result is not None:
            return result
        max_depth += 1

def depth_limited_search(initial_state, depth_limit):
    open_set = [eight_Puzzle(initial_state)]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return reconstruct_path(current_node)

        if current_node.g < depth_limit:
            closed_set.add(tuple(map(tuple, current_node.state)))
            for neighbor in get_position(current_node):
                if tuple(map(tuple, neighbor.state)) not in closed_set:
                    heapq.heappush(open_set, neighbor)

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append(node)
        node = node.parent
    path.reverse()
    return path

def print_path(path):
    for step, node in enumerate(path, start=1):
        print(f"Step {step}:")
        for row in node.state:
            print(" ".join(map(str, row)))
        print("")

if __name__ == "__main__":
    initial_state = [
        [1, 5, 3],
        [2, 7, 4],
        [6, 0, 8]
    ]

    solution = IDS_Search(initial_state)
    if solution:
        print("Solution found:")
        print_path(solution)
    else:
        print("No solution found.")

