def greedy(graph, start_zone, goal_zone):
    """
    Greedy algorithm to find a path using straight-line distance heuristic.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.

    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    open_list = set([start_zone])
    closed_list = set([])

    # Parents dictionary to keep track of the path
    parents = {}
    parents[start_zone] = start_zone

    # Track visited zones
    visited = set()

    while len(open_list) > 0:
        n = None

        # Find the node with the lowest heuristic value
        for v in open_list:
            if n is None or v.distanceToGoal < n.distanceToGoal:
                n = v

        if n is None:
            print('Path does not exist!')
            return None, visited, float('inf')

        # If the current node is the goal, reconstruct the path
        if n == goal_zone:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start_zone)
            reconst_path.reverse()

            return reconst_path, visited, calculate_cost(reconst_path)

        # For all neighbors of the current node
        for (m, road) in graph.get_connections(n):
            # If the current node is not in both open_list and closed_list
            # add it to open_list and note n as its parent
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n

        # Remove n from open_list and add it to closed_list
        # because all of its neighbors were inspected
        open_list.remove(n)
        closed_list.add(n)
        visited.add(n)

    print('Path does not exist!')
    return None, visited, float('inf')

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