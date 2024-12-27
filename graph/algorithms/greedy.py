import heapq
from graph.algorithms.heuristic import edge_heuristic

def greedy(graph, start_zone, goal_zone, weight_distance=0.5, weight_zone_heuristic=0.3, weight_edge=0.2):
    """
    Greedy algorithm to find the best path using a heuristic approach.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.
        weight_distance (float): Weight for the zone's distanceToGoal heuristic.
        weight_zone_heuristic (float): Weight for the zone's internal heuristic.
        weight_edge (float): Weight for the edge heuristic.

    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    open_set = [(0, start_zone)]
    heapq.heapify(open_set)
    came_from = {}
    visited = set()

    while open_set:
        current_f_score, current_zone = heapq.heappop(open_set)
        visited.add(current_zone)
        
        # Goal reached
        if current_zone == goal_zone:
            best_path = []
            total_cost = 0
            while current_zone in came_from:
                best_path.insert(0, current_zone)
                previous_zone = came_from[current_zone]
                road = next(road for neighbor, road in graph.get_connections(previous_zone) if neighbor == current_zone)
                total_cost += road.cost
                current_zone = previous_zone
            best_path.insert(0, start_zone)
            return best_path, visited, total_cost
        
        # Expand neighbors
        for neighbor, road in graph.get_connections(current_zone):
            if neighbor in visited:
                continue

            edge_heuristic_cost = edge_heuristic(road.cost, road.conditions, road.geography, road.infrastructure, road.availability)
            
            # Heuristic calculation
            h_score = (
                weight_distance * neighbor.distanceToGoal +
                weight_zone_heuristic * neighbor.heuristic +
                weight_edge * edge_heuristic_cost
            )
            
            came_from[neighbor] = current_zone
            heapq.heappush(open_set, (h_score, neighbor.name))  # Use neighbor.name for comparison

    return None, visited, float('inf')
