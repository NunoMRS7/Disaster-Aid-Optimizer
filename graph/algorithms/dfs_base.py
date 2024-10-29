def dfs(graph, start_zone, goal_zone):
    """
    Perform a Depth-First Search (DFS) traversal of a graph from a start zone to a goal zone.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The goal zone.

    Returns:
        tuple: A tuple containing the list of zones visited, the depth of the search, and the cost of the solution path.
    """
    stack = [(start_zone, [start_zone], 0)]
    zones_visited = []
    max_depth = 0
    solution_cost = 0

    while stack:
        current_zone, path, cost = stack.pop()
        
        if current_zone in zones_visited:
            continue
        
        zones_visited.append(current_zone)
        
        if current_zone == goal_zone:
            return zones_visited, len(path) - 1, cost
        
        for neighbor, travel_cost in graph.graph.get(current_zone, []):
            stack.append((neighbor, path + [neighbor], cost + travel_cost))
            max_depth = max(max_depth, len(path))
    
    return zones_visited, max_depth, solution_cost
