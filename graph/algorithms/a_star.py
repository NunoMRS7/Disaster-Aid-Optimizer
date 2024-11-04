import heapq
from graph.algorithms.heuristic import edge_heuristic

def a_star(graph, start_zone, goal_zone, weight_distance=0.5, weight_zone_heuristic=0.3, weight_edge=0.2):
    """
    A* algorithm to find the best path using a weighted heuristic approach.

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
    g_score = {zone: float('inf') for zone in graph.graph}
    g_score[start_zone] = 0

    best_path = []
    visited = set()

    while open_set:
        current_f_score, current_zone = heapq.heappop(open_set)
        visited.add(current_zone)
        
        # Goal reached
        if current_zone == goal_zone:
            best_path = []
            while current_zone in came_from:
                best_path.insert(0, current_zone)
                current_zone = came_from[current_zone]
            best_path.insert(0, start_zone)
            return best_path, visited, g_score[goal_zone]
        
        # Expand neighbors
        for neighbor, cost, *edge_data in graph.graph[current_zone]:
            edge_heuristic_cost = edge_heuristic(cost, *edge_data)
            
            tentative_g_score = g_score[current_zone] + edge_heuristic_cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_zone
                g_score[neighbor] = tentative_g_score
                
                # Heuristic calculation
                h_score = (
                    weight_distance * neighbor.distanceToGoal +
                    weight_zone_heuristic * neighbor.heuristic +
                    weight_edge * edge_heuristic_cost
                )
                f_score = tentative_g_score + h_score
                
                heapq.heappush(open_set, (f_score, neighbor))

    return None, visited, float('inf')
