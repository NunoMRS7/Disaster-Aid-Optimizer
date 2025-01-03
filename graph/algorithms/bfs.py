from queue import Queue

def bfs(graph, start_zone, goal_zone):
    """
    Breadth-First Search (BFS) algorithm to find the shortest path between zones.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.

    Returns:
        tuple: (path, visited_zones, total_cost)
    """
    visited = set()
    queue = Queue()
    cost = 0

    queue.put(start_zone)
    visited.add(start_zone)

    parent = dict()
    parent[start_zone] = None

    path_found = False
    while not queue.empty() and path_found == False:
        current_zone = queue.get()
        if current_zone == goal_zone:
            path_found = True
        else:
            for neighbor, road in graph.get_connections(current_zone):
                if neighbor not in visited:
                    queue.put(neighbor)
                    parent[neighbor] = current_zone 
                    visited.add(neighbor)

    path = []
    if path_found:
        path.append(goal_zone)
        while parent[goal_zone] is not None:
            path.append(parent[goal_zone])
            goal_zone = parent[goal_zone]
        path.reverse()    
        cost = calculate_cost(path)
        return path, visited, cost
    
    return None, None, None

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
