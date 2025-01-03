def dfs(graph, start_zone, goal_zone):
    """
    Depth-First Search algorithm to find the best path in terms of minimum cost.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.

    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    path = []
    visited = set()
    return dfs_recursive(graph, start_zone, goal_zone, path, visited)

def dfs_recursive(graph, start_zone, goal_zone, path, visited):
    """
    Recursive helper function for the Depth-First Search algorithm.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.
        path (list): The current path.
        visited (set): The set of visited zones.
    
    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    path.append(start_zone)
    visited.add(start_zone)

    if start_zone == goal_zone:
        cost = calculate_cost(path)
        return path, visited, cost
    
    for neighbor, road in graph.get_connections(start_zone):
        if neighbor not in visited:
            best_path, zone_visited, current_cost = dfs_recursive(graph, neighbor, goal_zone, path, visited)
            if best_path is not None:
                return best_path, zone_visited, current_cost
    
    path.pop()
    return None, visited, 0

def calculate_cost(path):
    """
    Calculate the total cost of the path.

    Args:
        path (list): The path to calculate the cost for.

    Returns:
        float: The total cost of the path.
    """
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += path[i].calculate_distance_between_zones(path[i + 1])
    return total_cost
