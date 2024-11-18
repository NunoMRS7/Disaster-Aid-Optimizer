import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from enums.severity import Severity
from core.zone import Zone
from utils.coordinate import Coordinate
from core.road import Road
from enums.conditions import Conditions
from enums.geography import Geography
from enums.infrastructure import Infrastructure

# Constants
DEFAULT_NODE_SIZE = 50  # Default size for nodes with N/A population
MAX_POPULATION = 1e7  # Scale factor for node size based on population
POPULATION_SCALE = 5000  # Scale factor for node size based on population

# Load municipalities from JSON file
def load_municipalities_from_json(graph, filename):
    with open(filename, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
        for name, info in data.items():
            latitude, longitude = info["centroide"]
            population = info.get("population", None)  # Read population

            # Convert population to integer or set to 0 if it's None or N/A
            if population is None or population == "N/A":
                population = 0
            else:
                try:
                    population = int(population)  # Ensure population is an integer
                except ValueError:
                    population = 0  # In case of any unexpected string format

            coordinate = Coordinate(latitude, longitude)

            zone = Zone()
            zone.name = name
            zone.coordinate = coordinate
            zone.population = population

            graph.add_zone(zone)
        
def load_roads_from_json(graph, filename):
    with open(filename, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
        for name, info in data.items():
            for neighbor_name in info["vizinhos"]:
                zone = graph.get_zone(name)
                neighbor = graph.get_zone(neighbor_name)

                if zone and neighbor:
                    # Check if the connection already exists to avoid duplication
                    if not graph.has_connection(zone, neighbor):
                        road = Road()
                        road.cost = zone.calculate_distance_between_zones(neighbor)
                        road.geography = random.choice(list(Geography))
                        road.infrastructure = random.choice(list(Infrastructure))

                        graph.add_connection(zone, neighbor, road)
                

# Visualize the graph with NetworkX and Matplotlib
def visualize_generated_graph(graph, show_labels=False, show_conditions=False, show_geography=False, show_infrastructure=False, show_cost=False):
    G = nx.Graph()
    pos = {}
    node_sizes = []

    # Set up nodes with positions and sizes
    for zone in graph.graph.keys():
        G.add_node(zone.name)
        pos[zone.name] = (zone.coordinate.longitude, zone.coordinate.latitude)
        
        # Calculate size based on population, use default if population is 0
        if zone.population > 0:
            size = (zone.population / MAX_POPULATION) * POPULATION_SCALE
        else:
            size = DEFAULT_NODE_SIZE
            
        node_sizes.append(size)

    # Add edges for neighbor connections with colors
    for zone, connections in graph.graph.items():
        for neighbor, road in connections:
            G.add_edge(zone.name, neighbor.name, availability=road.availability)

    # Determine edge colors based on availability attribute
    edge_colors = ["green" if G[node1][node2]['availability'] else "red" for node1, node2 in G.edges()]

    # Rescale positions for centering
    pos_array = np.array(list(pos.values()))
    pos_normalized = nx.rescale_layout(pos_array, scale=1.0)
    pos = {node: pos_normalized[i] for i, node in enumerate(pos.keys())}

    # Plot settings
    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="blue", alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=0.5, edge_color=edge_colors, style=["solid" if avail else "dashed" for avail in nx.get_edge_attributes(G, "availability").values()])

    # Option to show or hide labels
    if show_labels:
        nx.draw_networkx_labels(G, pos, font_size=4, font_color="white",
                                verticalalignment="center",
                                bbox=dict(facecolor="blue", edgecolor="none", boxstyle="round,pad=0.2"))

    # Option to show conditions, geography, infrastructure, and cost
    if show_conditions or show_geography or show_infrastructure or show_cost:
        for zone, connections in graph.graph.items():
            for neighbor, road in connections:
                mid_x, mid_y = (pos[zone.name][0] + pos[neighbor.name][0]) / 2, (pos[zone.name][1] + pos[neighbor.name][1]) / 2
                text_y_offset = 0
                if show_conditions:
                    plt.text(mid_x, mid_y + text_y_offset, f"{road.conditions}", color="orange", fontsize=6, ha='center', va='center')
                    text_y_offset -= 0.1
                if show_geography:
                    plt.text(mid_x, mid_y + text_y_offset, f"{road.geography}", color="brown", fontsize=6, ha='center', va='center')
                    text_y_offset -= 0.1
                if show_infrastructure:
                    plt.text(mid_x, mid_y + text_y_offset, f"{road.infrastructure}", color="purple", fontsize=6, ha='center', va='center')
                    text_y_offset -= 0.1
                if show_cost:
                    plt.text(mid_x, mid_y + text_y_offset, f"{road.cost:.2f}", color="black", fontsize=6, ha='center', va='center')

    plt.title("Portugal Municipalities Graph (Continental Only)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis("equal")  # Keep x and y scales equal for better visualization
    plt.tight_layout()  # Adjust layout to fit everything within the plot
    plt.show()

