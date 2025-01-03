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

    # Step 1: Create zones (nodes)
    for _ in range(num_nodes):
        zone = Zone()
        zone.name = name_generator.generate_name()
        zone.coordinate = Coordinate(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
        zone.population = random.randint(1000, 100000)

        zones.append(zone)
        graph.add_zone(zone)

    # Step 2: Ensure graph connectivity using a spanning tree
    unvisited = set(zones)
    visited = set()
    current_zone = unvisited.pop()
    visited.add(current_zone)

    while unvisited:
        target_zone = random.choice(list(unvisited))
        road = Road()
        road.cost = current_zone.calculate_distance_between_zones(target_zone)
        road.geography = random.choice(list(Geography))
        road.infrastructure = random.choice(list(Infrastructure))

        graph.add_connection(current_zone, target_zone, road)
        visited.add(target_zone)
        unvisited.remove(target_zone)
        current_zone = target_zone

    # Step 3: Add random connections for realism
    for _ in range(num_nodes):  # Limit number of random connections
        zone_a, zone_b = random.sample(zones, 2)
        if not graph.has_connection(zone_a, zone_b):  # Check for existing connection
            road = Road()
            road.cost = zone_a.calculate_distance_between_zones(zone_b)
            road.geography = random.choice(list(Geography))
            road.infrastructure = random.choice(list(Infrastructure))

            graph.add_connection(zone_a, zone_b, road)

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
