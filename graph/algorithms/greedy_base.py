import heapq

def greedy_search(graph, start_zone, goal_zone, heuristic):
    """
    Perform a Greedy Search traversal of a graph from a start zone to a goal zone.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The goal zone.
        heuristic (function): A function that estimates the cost from the current zone to the goal.

    Returns:
        tuple: A tuple containing the list of zones visited, the depth of the search, and the cost of the solution path.
    """
    # Ensure that start_zone and goal_zone are not None
    if start_zone is None or goal_zone is None:
        raise ValueError("Start zone and goal zone must be valid Zone instances.")

    # Initialize the priority queue with the heuristic for the start zone
    priority_queue = [(heuristic(start_zone, goal_zone), start_zone, [start_zone], 0)]
    zones_visited = []

    while priority_queue:
        _, current_zone, path, cost = heapq.heappop(priority_queue)

        if current_zone in zones_visited:
            continue
        
        zones_visited.append(current_zone)
        
        # If we reach the goal zone, return the path
        if current_zone == goal_zone:
            return zones_visited, len(path), cost
        
        # Check neighbors and add them to the queue
        for neighbor, travel_cost in graph.graph.get(current_zone, []):
            if neighbor not in zones_visited:  # Prevent revisiting zones
                new_cost = cost + travel_cost
                priority = heuristic(neighbor, goal_zone, travel_cost)  # Use only the heuristic value
                heapq.heappush(priority_queue, (priority, neighbor, path + [neighbor], new_cost))

    return zones_visited, 0, 0  # Return empty if goal is not found
