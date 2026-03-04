#Aditya Seshadri- se24ucse012
#Q3 DFS,BFS,variants

from collections import deque
start = (3, 3, 1)
goal = (0, 0, 0)

def is_valid(state):
    m, c, b = state
    m_right = 3 - m
    c_right = 3 - c
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def get_successors(state):
    m, c, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    successors = []
    for move in moves:
        m_move, c_move = move
        if boat == 1:
            new_state = (m - m_move, c - c_move, 0)
        else:
            new_state = (m + m_move, c + c_move, 1)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes = 0
    while queue:
        state, path = queue.popleft()
        nodes += 1
        if state == goal:
            return path, nodes
        visited.add(state)
        for next_state in get_successors(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None, nodes

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes = 0
    while stack:
        state, path = stack.pop()
        nodes += 1
        if state == goal:
            return path, nodes
        visited.add(state)
        for next_state in get_successors(state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))
    return None, nodes

def dls(state, goal, limit, path, visited, nodes):
    nodes[0] += 1
    if state == goal:
        return path
    if limit <= 0:
        return None
    visited.add(state)
    for next_state in get_successors(state):
        if next_state not in visited:
            result = dls(next_state, goal, limit-1,
                         path + [next_state], visited, nodes)
            if result:
                return result

    return None

def ids(start, goal, max_depth=20):
    total_nodes = 0
    for depth in range(max_depth):
        nodes = [0]
        visited = set()
        result = dls(start, goal, depth, [start], visited, nodes)
        total_nodes += nodes[0]
        if result:
            return result, total_nodes
    return None, total_nodes

print("\nMissionaries and Cannibals Problem\n")

bfs_path, bfs_nodes = bfs(start, goal)
print("BFS Solution:")
for state in bfs_path:
    print(state)
print("Nodes explored:", bfs_nodes)
print("Solution depth:", len(bfs_path)-1)
print("\n---------------------------------\n")

dfs_path, dfs_nodes = dfs(start, goal)
print("DFS Solution:")
for state in dfs_path:
    print(state)
print("Nodes explored:", dfs_nodes)
print("Solution depth:", len(dfs_path)-1)
print("\n---------------------------------\n")

ids_path, ids_nodes = ids(start, goal)

print("Iterative Deepening Solution:")
for state in ids_path:
    print(state)

print("Nodes explored:", ids_nodes)
print("Solution depth:", len(ids_path)-1)
print("\n---------------------------------\n")

print("Performance Comparison")
print("BFS: Guarantees shortest path but uses more memory.")
print("DFS: Uses less memory but may not find optimal solution.")
print("DLS: DFS with depth limit to avoid infinite paths.")
print("IDS: Combines advantages of BFS and DFS.")


print("\n---------------------------------")
print("Performance Comparison")

print("BFS explored", bfs_nodes, "nodes and found solution depth", len(bfs_path)-1)
print("DFS explored", dfs_nodes, "nodes and found solution depth", len(dfs_path)-1)
print("IDS explored", ids_nodes, "nodes and found solution depth", len(ids_path)-1)

print("\nConclusion:")
print("BFS guarantees the shortest path but uses more memory.")
print("DFS uses less memory but may not find the optimal solution.")
print("Iterative Deepening combines advantages of BFS and DFS.")
