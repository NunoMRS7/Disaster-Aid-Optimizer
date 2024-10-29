import heapq

def a_star(graph, start_zone, goal_zone, heuristic):
    """
    Perform an A* Search traversal of a graph from a start zone to a goal zone.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The goal zone.
        heuristic (function): A function that estimates the cost from the current zone to the goal.

    Returns:
        tuple: A tuple containing the list of zones visited, the depth of the search, and the cost of the solution path.
    """
    priority_queue = [(0 + heuristic(start_zone, goal_zone), start_zone, [start_zone], 0)]
    zones_visited = []
    max_depth = 0

    while priority_queue:
        _, current_zone, path, cost = heapq.heappop(priority_queue)
        
        if current_zone in zones_visited:
            continue
        
        zones_visited.append(current_zone)
        
        if current_zone == goal_zone:
            return zones_visited, len(path) - 1, cost
        
        for neighbor, travel_cost in graph.graph.get(current_zone, []):
            new_cost = cost + travel_cost
            priority = new_cost + heuristic(neighbor, goal_zone)
            heapq.heappush(priority_queue, (priority, neighbor, path + [neighbor], new_cost))
            max_depth = max(max_depth, len(path))
    
    return zones_visited, max_depth, 0
