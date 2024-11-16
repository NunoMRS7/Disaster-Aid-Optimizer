import random
from graph.graph_builder import Graph
from core.zone import Zone
from enums.geography import Geography
from enums.severity import Severity
from enums.conditions import Conditions
from enums.infrastructure import Infrastructure
from utils.name_generator import NameGenerator
from utils.coordinate import Coordinate
from core.road import Road

def generate_random_graph(num_nodes: int) -> Graph:
    """
    Generates a random graph with a specified number of nodes and random edge properties, ensuring each zone has at least one connection.

    Args:
        num_nodes (int): Number of nodes to include in the graph.

    Returns:
        Graph: A randomly generated graph with specified nodes and edges with random properties.
    """
    graph = Graph()
    name_generator = NameGenerator()
    zones = []

    # Create random zones as graph nodes
    for _ in range(num_nodes):
        name = name_generator.generate_name()
        coordinate = Coordinate(random.uniform(-90, 90), random.uniform(-180, 180))
        severity = random.choice(list(Severity))
        population = random.randint(1000, 100000)
        
        zone = Zone(name, coordinate, severity, population)
        zones.append(zone)
        graph.add_zone(zone)
    
    # Connect zones with random edge properties
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() > 0.5:  # 50% chance to create an edge
                road = Road()
                road.cost = random.uniform(10.0, 100.0)
                road.conditions = random.choice(list(Conditions))
                road.geography = random.choice(list(Geography))
                road.infrastructure = random.choice(list(Infrastructure))
                road.availability = random.choices([True, False], weights=[0.7, 0.3])[0]

                graph.add_connection(zones[i], zones[j], road)

    # Ensure every zone has at least one connection
    for zone in zones:
        if not graph.graph[zone]:  # Check if the zone has no connections
            # Choose another random zone to connect with
            target_zone = random.choice([z for z in zones if z != zone])
            road = Road()
            road.cost = random.uniform(10.0, 100.0)
            road.conditions = random.choice(list(Conditions))
            road.geography = random.choice(list(Geography))
            road.infrastructure = random.choice(list(Infrastructure))
            road.availability = random.choices([True, False], weights=[0.7, 0.3])[0]

            # Create a connection between the isolated zone and the chosen target zone
            graph.add_connection(zone, target_zone, road)
    
    return graph
