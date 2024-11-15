import json
import networkx as nx
import matplotlib.pyplot as plt
import argparse
import numpy as np

# Constants
DEFAULT_NODE_SIZE = 50  # Default size for nodes with N/A population
MAX_POPULATION = 1e7  # Scale factor for node size based on population
POPULATION_SCALE = 5000  # Scale factor for node size based on population

# Updated Municipality Node Class
class MunicipalityNode:
    def __init__(self, name, latitude, longitude, population):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.population = population  # Population attribute
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

# Graph Class to Store Municipalities
class PortugalGraph:
    def __init__(self):
        self.nodes = {}

    def add_municipality(self, name, latitude, longitude, population):
        node = MunicipalityNode(name, latitude, longitude, population)
        self.nodes[name] = node

    def add_edge(self, municipality1, municipality2):
        if municipality1 in self.nodes and municipality2 in self.nodes:
            self.nodes[municipality1].add_neighbor(self.nodes[municipality2])
            self.nodes[municipality2].add_neighbor(self.nodes[municipality1])

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

            graph.add_municipality(name, latitude, longitude, population)

            # Add edges based on neighbors
            for neighbor in info["vizinhos"]:
                graph.add_edge(name, neighbor)

# Visualize the graph with NetworkX and Matplotlib
def visualize_graph(graph, show_labels):
    G = nx.Graph()
    pos = {}
    node_sizes = []

    # Set up nodes with positions and sizes
    for node in graph.nodes.values():
        G.add_node(node.name)
        pos[node.name] = (node.longitude, node.latitude)
        
        # Calculate size based on population, use default if population is 0
        if node.population > 0:
            size = (node.population / MAX_POPULATION) * POPULATION_SCALE
        else:
            size = DEFAULT_NODE_SIZE
            
        node_sizes.append(size)

    # Add edges for neighbor connections
    for node in graph.nodes.values():
        for neighbor in node.neighbors:
            G.add_edge(node.name, neighbor.name)

    # Rescale positions for centering
    pos_array = np.array(list(pos.values()))
    pos_normalized = nx.rescale_layout(pos_array, scale=1.0)
    pos = {node: pos_normalized[i] for i, node in enumerate(pos.keys())}

    # Plot settings
    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="blue", alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5)

    # Option to show or hide labels
    if show_labels:
        nx.draw_networkx_labels(G, pos, font_size=4, font_color="white",
                                verticalalignment="center",
                                bbox=dict(facecolor="blue", edgecolor="none", boxstyle="round,pad=0.2"))

    plt.title("Portugal Municipalities Graph (Continental Only)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis("equal")  # Keep x and y scales equal for better visualization
    plt.show()

# Main function
def main():
    parser = argparse.ArgumentParser(description="Portugal Municipalities Graph Visualization")
    parser.add_argument("--show-labels", action="store_true",
                        help="If set, display names. Otherwise, labels are hidden.")
    args = parser.parse_args()

    portugal_graph = PortugalGraph()

    # Load municipalities from JSON file
    load_municipalities_from_json(portugal_graph, "data/after/final_output.json")

    # Visualize the graph with the show_labels argument
    visualize_graph(portugal_graph, args.show_labels)

if __name__ == "__main__":
    main()
