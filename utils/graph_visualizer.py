import matplotlib.pyplot as plt
from graph.graph_builder import Graph
import random

def print_graph(graph: Graph):
    """
    Prints a textual representation of the graph showing nodes and their connections.

    Args:
        graph (Graph): The graph to print.
    """
    for zone, connections in graph.graph.items():
        print(f"Zone {zone.geography} ({zone.severity}):")
        for neighbor, cost in connections:
            print(f"  -> Connected to {neighbor.geography} with cost {cost:.2f} km")

def visualize_graph(graph: Graph):
    """
    Visualizes the graph using matplotlib, with nodes and weighted edges.

    Args:
        graph (Graph): The graph to visualize.
    """
    plt.figure(figsize=(8, 6))
    pos = {}
    edges = []
    labels = {}

    # Position nodes randomly for display
    for idx, (zone, connections) in enumerate(graph.graph.items()):
        pos[zone] = (random.uniform(0, 10), random.uniform(0, 10))
        labels[zone] = f"{zone.geography.name}"

        for neighbor, cost in connections:
            edges.append((zone, neighbor, cost))

    # Plot nodes
    for node, (x, y) in pos.items():
        plt.scatter(x, y, s=100)
        plt.text(x, y, labels[node], fontsize=12, ha='right')

    # Plot edges with weights
    for start, end, cost in edges:
        x_values = [pos[start][0], pos[end][0]]
        y_values = [pos[start][1], pos[end][1]]
        plt.plot(x_values, y_values, 'b-', linewidth=1)
        mid_x, mid_y = (x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2
        plt.text(mid_x, mid_y, f"{cost:.2f}", color="red", fontsize=9)
    
    plt.title("Graph Visualization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
