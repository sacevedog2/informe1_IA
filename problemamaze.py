import heapq  # El módulo heapq implementa colas de prioridad (heaps)

class Node:
    def __init__(self, position, parent=None, path_cost=0):
        self.position = position
        self.parent = parent
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, maze):
        self.maze = maze
        self.actions = {
            (-1, 0): "Up",
            (1, 0): "Down",
            (0, -1): "Left",
            (0, 1): "Right"
        }

    def is_valid(self, pos):
        rows = len(self.maze)
        cols = len(self.maze[0])
        r, c = pos
        return 0 <= r < rows and 0 <= c < cols and self.maze[r][c] != "#"

def find_exit(maze):
    start = (1, 1)  # Posición inicial (S)
    end = (1, 6)    # Posición final (E)

    problem = Problem(maze)  # Se crea el problema con el laberinto

    def manhatan_distance(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])  # Distancia de Manhattan

    def get_neighbors(pos):
        neighbors = []
        for move in problem.actions.keys():
            neighbor = (pos[0] + move[0], pos[1] + move[1])
            if problem.is_valid(neighbor):
                neighbors.append(neighbor)
        return neighbors

    start_node = Node(start, path_cost=0)
    frontier = [(manhatan_distance(start, end), start_node)]
    heapq.heapify(frontier)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node.position == end:
            return reconstruct_path(node)

        for neighbor in get_neighbors(node.position):
            new_cost = node.path_cost + 1
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, path_cost=new_cost)
                heapq.heappush(frontier, (manhatan_distance(neighbor, end), reached[neighbor]))

    return None  # No se encontró salida

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    path.reverse()
    return path

# Laberinto de prueba
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", "#", " ", "#", " ", "E", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]

path = find_exit(maze)
print("Path to exit:", path)