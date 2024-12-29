import heapq
from graph.algorithms.heuristic import edge_heuristic
from utils.graph_generator import apply_randomness_to_graph
from map.src.plot_portugal_graph import visualize_generated_graph

class ZoneWrapper:
    def __init__(self, f_score, zone):
        self.f_score = f_score
        self.zone = zone

    def __lt__(self, other):
        return self.f_score < other.f_score

def a_star(graph, start_zone, goal_zone, use_simple_heuristic=True, weight_distance=0.5, weight_zone_heuristic=0.3, weight_edge=0.2):
    """
    A* algorithm to find the best path using either a simple or a weighted heuristic approach.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.
        use_simple_heuristic (bool): If True, use a simple heuristic; otherwise, use a weighted heuristic.
        weight_distance (float): Weight for the zone's distanceToGoal heuristic (used if use_simple_heuristic is False).
        weight_zone_heuristic (float): Weight for the zone's internal heuristic (used if use_simple_heuristic is False).
        weight_edge (float): Weight for the edge heuristic (used if use_simple_heuristic is False).

    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    open_set = [ZoneWrapper(0, start_zone)]
    heapq.heapify(open_set)
    came_from = {}
    g_score = {zone: float('inf') for zone in graph.graph}
    g_score[start_zone] = 0

    best_path = []
    visited = set()

    iteration_count = 1

    while open_set:
        if not use_simple_heuristic and iteration_count % 3 == 0:
            apply_randomness_to_graph(graph)

        current_wrapper = heapq.heappop(open_set)
        current_f_score, current_zone = current_wrapper.f_score, current_wrapper.zone
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
        for neighbor, road in graph.get_connections(current_zone):
            tentative_g_score = g_score[current_zone] + road.cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_zone
                g_score[neighbor] = tentative_g_score
                
                # Heuristic calculation
                if use_simple_heuristic:
                    h_score = neighbor.distanceToGoal
                else:
                    edge_heuristic_cost = edge_heuristic(road.cost, road.conditions, road.geography, road.infrastructure, road.availability)
                    h_score = (
                        weight_distance * neighbor.distanceToGoal +
                        weight_zone_heuristic * neighbor.heuristic +
                        weight_edge * edge_heuristic_cost
                    )
                f_score = tentative_g_score + h_score
                
                heapq.heappush(open_set, ZoneWrapper(f_score, neighbor))
        
        iteration_count += 1

    return None, visited, float('inf')
