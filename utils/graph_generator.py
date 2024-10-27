import random
from graph.graph_builder import Graph
from core.zone import Zone
from enums.geography import GeographyType
from enums.rating import Rating

def generate_random_graph(num_nodes: int) -> Graph:
    """
    Generates a random graph with a specified number of nodes and random edge costs.

    Args:
        num_nodes (int): Number of nodes to include in the graph.

    Returns:
        Graph: A randomly generated graph with specified nodes and edges with random costs.
    """
    graph = Graph()
    zones = []

    # Create random zones as graph nodes
    for _ in range(num_nodes):
        geography = random.choice(list(GeographyType))
        severity = random.choice(list(Rating))
        population = random.randint(1000, 10000)
        zone = Zone(geography, severity, population)
        zones.append(zone)
        graph.add_zone(zone)
    
    # Connect zones with random costs
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() > 0.5:  # 50% chance to create an edge
                cost = random.uniform(10.0, 100.0)  # Cost between 10 and 100
                graph.add_connection(zones[i], zones[j], cost)
    
    return graph
