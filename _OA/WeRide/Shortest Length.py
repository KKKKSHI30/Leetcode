from collections import defaultdict, deque
def bfs_distance(tree, start):
    visited = set([start])
    distances = {node: float('inf') for node in tree}
    distances[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if neighbor not in visited:
                distances[neighbor] = distances[node] + 1
                visited.add(neighbor)
                queue.append(neighbor)
    return distances
def find_LCA(u, v, parents, levels):
    # If v is deeper than u in the tree, swap them
    if levels[u] < levels[v]:
        u, v = v, u
    # Ascend from the deeper node until they are at the same level
    while levels[u] != levels[v]:
        u = parents[u]
    # Ascend in the tree until we find the LCA
    while u != v:
        u = parents[u]
        v = parents[v]
    return u
def minimumTreePath(n, edges, visitNodes):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    distances_from_start = bfs_distance(tree, 1)
    nodes = [1] + visitNodes + [n]
    total_dist = 0
    # Find parent and level of each node using BFS
    parents = {}
    levels = {}
    visited = set()
    queue = deque([(1, 0)])
    while queue:
        node, level = queue.popleft()
        visited.add(node)
        levels[node] = level
        for neighbor in tree[node]:
            if neighbor not in visited:
                parents[neighbor] = node
                queue.append((neighbor, level + 1))
    for i in range(1, len(nodes)):
        lca = find_LCA(nodes[i-1], nodes[i], parents, levels)
        # Use LCA to compute the distance between two nodes
        total_dist += distances_from_start[nodes[i-1]] + distances_from_start[nodes[i]] - 2 * distances_from_start[lca]
    return total_dist