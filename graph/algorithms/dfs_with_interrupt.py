from core.zone import Zone
from utils.graph_visualizer import GraphVisualizer

def dfs_with_interrupt(graph, start_zone, vehicle, visualizer: GraphVisualizer = None):
    """
    Traverse the graph from a start zone while considering vehicle autonomy.

    Args:
        graph (Graph): The graph containing zones and connections.
        start_zone (Zone): The starting zone.
        vehicle (Vehicle): The vehicle to traverse with.
        visualizer (GraphVisualizer, optional): The visualizer to use for visualization.

    Returns:
        list: List of zones visited.
    """
    visited = []
    stack = [(start_zone, vehicle.autonomy)]
    
    if visualizer:
        visualizer.set_stack(stack)
    
    while stack:
        current_zone, remaining_autonomy = stack.pop()
        
        if current_zone in visited:
            continue
        
        visited.append(current_zone)
        if visualizer:
            visualizer.visualize_step(current_zone)
        
        print(f"Visiting {current_zone.geography} with remaining autonomy: {remaining_autonomy:.2f} km")
        
        for neighbor, cost in graph.graph.get(current_zone, []):
            if remaining_autonomy >= cost:
                stack.append((neighbor, remaining_autonomy - cost))
    
    return visited