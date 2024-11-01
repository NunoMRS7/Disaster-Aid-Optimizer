from collections import deque

def bfs(graph, start_zone, goal_zone):
    """
    Breadth-First Search (BFS) algorithm to find the shortest path between zones.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.

    Returns:
        tuple: (path, visited_zones, max_depth, total_cost)
    """
    queue = deque([(start_zone, [start_zone], 0, 0)])
    visited = set()
    max_depth = 0
    total_cost = 0
    visited_zones = set()

    while queue:
        current_zone, path, depth, cost = queue.popleft()
        visited.add(current_zone)
        visited_zones.add(current_zone)
        max_depth = max(max_depth, depth)

        if current_zone == goal_zone:
            return path, visited_zones, max_depth, cost

        for neighbor, edge_cost, _, _, _, availability in graph.graph[current_zone]:
            if neighbor not in visited and availability:
                new_cost = cost + edge_cost
                queue.append((neighbor, path + [neighbor], depth + 1, new_cost))

    return [], visited_zones, max_depth, total_cost
