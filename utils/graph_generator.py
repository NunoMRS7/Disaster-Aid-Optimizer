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
from map.src.plot_portugal_graph import load_municipalities_from_json
from map.src.plot_portugal_graph import load_roads_from_json


data_path = "map/data/after/final_output.json"

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
        zone = Zone()
        zone.name = name_generator.generate_name()
        zone.coordinate = Coordinate(random.uniform(-90, 90), random.uniform(-180, 180))
        zone.population = random.randint(1000, 100000)

        zones.append(zone)
        graph.add_zone(zone)

    # Connect zones with random edge properties
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() > 0.5:  # 50% chance to create an edge
                road = Road()
                road.cost = random.uniform(10.0, 100.0)
                road.geography = random.choice(list(Geography))
                road.infrastructure = random.choice(list(Infrastructure))

                graph.add_connection(zones[i], zones[j], road)

    # Ensure every zone has at least one connection
    for zone in zones:
        if not graph.graph[zone]:  # Check if the zone has no connections
            # Choose another random zone to connect with
            target_zone = random.choice([z for z in zones if z != zone])
            road = Road()
            road.cost = random.uniform(10.0, 100.0)
            road.geography = random.choice(list(Geography))
            road.infrastructure = random.choice(list(Infrastructure))

            # Create a connection between the isolated zone and the chosen target zone
            graph.add_connection(zone, target_zone, road)

    return graph


def generate_map_graph() -> Graph:
    """
    Generates a map graph with predefined nodes and edges.

    Returns:
        Graph: A map graph with predefined nodes and edges.
    """
    graph = Graph()

    load_municipalities_from_json(graph, data_path)

    load_roads_from_json(graph, data_path)

    return graph


def apply_randomness_to_graph(graph):
    for zone in graph.graph:
        apply_randomness_to_zone(zone)
        for _,road in graph.graph[zone]:
            apply_randomness_to_road(road)


def apply_randomness_to_road(road):
    road.conditions = random.choice(list(Conditions))
    road.availability = random.choices([True, False], weights=[0.7, 0.3])[0]


def apply_randomness_to_zone(zone):
    random.choice(list(Severity))
