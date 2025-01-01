import heapq
from graph.algorithms.heuristic import edge_heuristic

def greedy(graph, start_zone, goal_zone, use_simple_heuristic=True, vehicle=None):
    """
    Greedy algorithm to find a path using a heuristic-driven approach.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        goal_zone (Zone): The target zone.
        use_simple_heuristic (bool): Whether to use the simple heuristic.
        vehicle (Vehicle): The vehicle being used for traversal.

    Returns:
        tuple: (best_path, visited_zones, total_cost)
    """
    open_set = []
    heapq.heappush(open_set, (0, id(start_zone), start_zone))  # Add id to avoid direct Zone comparison
    came_from = {}
    visited = set()

    # Track costs
    cost_so_far = {zone: float('inf') for zone in graph.graph}
    cost_so_far[start_zone] = 0

    while open_set:
        current_h_score, _, current_zone = heapq.heappop(open_set)
        visited.add(current_zone)

        # Goal reached
        if current_zone == goal_zone:
            best_path = []
            while current_zone in came_from:
                best_path.insert(0, current_zone)
                current_zone = came_from[current_zone]
            best_path.insert(0, start_zone)
            return best_path, visited, cost_so_far[goal_zone]
        
        # Expand neighbors
        for neighbor, road in graph.get_connections(current_zone):
            if neighbor not in visited:
                # Heuristic calculation
                if use_simple_heuristic:
                    h_score = neighbor.distanceToGoal
                else:
                    h_score = neighbor.heuristic

                # Update cost if this path is better
                edge_cost = edge_heuristic(road.cost, road.conditions, road.geography, road.infrastructure, road.availability, vehicle.type if vehicle else None)
                total_cost = cost_so_far[current_zone] + edge_cost

                if total_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = total_cost
                    heapq.heappush(open_set, (h_score, id(neighbor), neighbor))
                    came_from[neighbor] = current_zone

    return None, visited, float('inf')