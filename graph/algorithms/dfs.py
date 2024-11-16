def dfs(graph, start_zone, goal_zone):
    """
    Depth-First Search algorithm to find the best path in terms of minimum cost (iterative version).

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.

    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    stack = [(start_zone, [start_zone], 0)]  # Stack holds tuples of (current_zone, path, current_cost)
    visited_zones = set()
    best_path = None
    min_cost = float('inf')
    
    while stack:
        current_zone, path, current_cost = stack.pop()
        
        if current_zone in visited_zones:
            continue
        
        visited_zones.add(current_zone)
        
        # If the goal zone is reached, check if this path is the minimum cost path
        if current_zone == goal_zone:
            if current_cost < min_cost:
                best_path = path
                min_cost = current_cost
            continue

        # Explore neighbors of the current zone
        for neighbor, road in graph.get_connections(current_zone):
            if neighbor not in visited_zones and road.availability:
                total_cost = current_cost + road.cost
                stack.append((neighbor, path + [neighbor], total_cost))

    return best_path, visited_zones, min_cost
