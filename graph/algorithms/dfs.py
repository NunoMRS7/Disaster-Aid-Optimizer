def dfs(graph, start_zone, goal_zone):
    """
    Depth-First Search algorithm to find the best path in terms of minimum cost.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.

    Returns:
        tuple: (best_path, visited_zones, max_depth, total_cost)
    """
    visited = set()
    best_path = []
    best_cost = float('inf')
    max_depth = 0

    def dfs_recursive(zone, path, depth, cost):
        nonlocal best_path, best_cost, max_depth

        # Update max depth
        max_depth = max(max_depth, depth)
        
        # Base case: if goal reached
        if zone == goal_zone:
            if cost < best_cost:
                best_cost = cost
                best_path = path[:]
            return

        # Visit neighbors
        for neighbor, edge_cost, _, _, _, _ in graph.graph[zone]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                
                dfs_recursive(neighbor, path, depth + 1, cost + edge_cost)
                
                path.pop()
    
    visited.add(start_zone)
    dfs_recursive(start_zone, [start_zone], 0, 0)
    
    return best_path, visited, max_depth, best_cost
