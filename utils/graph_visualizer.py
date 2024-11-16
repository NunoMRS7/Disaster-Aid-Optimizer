import matplotlib.pyplot as plt
from graph.graph_builder import Graph
import random
from core.road import Road

def print_graph(graph: Graph):
    """
    Prints a structured representation of the graph, showing zones and their connections with properties.

    Args:
        graph (Graph): The graph to print.
    """
    for zone, connections in graph.graph.items():
        print(f"Zone {zone.name} (Severity: {zone.severity}, Population: {zone.population}):")
        for neighbor, road in connections:
            print(
                f"  -> Connected to {neighbor.name}:\n"
                f"       Cost           : {road.cost:.2f} km\n"
                f"       Conditions     : {road.conditions}\n"
                f"       Geography      : {road.geography}\n"
                f"       Infrastructure : {road.infrastructure}\n"
                f"       Available      : {'Yes' if road.availability else 'No'}\n"
            )


def visualize_graph(graph: Graph):
    """
    Visualizes the graph using matplotlib, with nodes and detailed edge properties.

    Args:
        graph (Graph): The graph to visualize.
    """
    plt.figure(figsize=(10, 8))
    pos = {}
    edges = []
    labels = {}

    # Position nodes randomly for display
    for idx, (zone, connections) in enumerate(graph.graph.items()):
        pos[zone] = (random.uniform(0, 10), random.uniform(0, 10))
        labels[zone] = f"{zone.name} (S:{zone.severity.value}, P:{zone.population})"

        for neighbor, road in connections:
            edges.append((zone, neighbor, road))

    # Plot nodes
    for node, (x, y) in pos.items():
        plt.scatter(x, y, s=100, label=node.name)
        plt.text(x, y, labels[node], fontsize=10, ha='right')

    # Plot edges with detailed information
    for start, end, road in edges:
        x_values = [pos[start][0], pos[end][0]]
        y_values = [pos[start][1], pos[end][1]]
        color = "green" if road.availability else "gray"  # Available connections in green, others in gray
        plt.plot(x_values, y_values, color=color, linestyle='-', linewidth=1)

        # Midpoint of edge for displaying detailed information
        mid_x, mid_y = (x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2
        plt.text(mid_x, mid_y, f"{road.cost:.2f} km", color="blue", fontsize=8)
        plt.text(mid_x, mid_y - 0.2, f"{road.infrastructure}", color="purple", fontsize=8)
        plt.text(mid_x, mid_y - 0.4, f"{road.conditions}", color="orange", fontsize=8)
        plt.text(mid_x, mid_y - 0.6, f"{road.geography}", color="brown", fontsize=8)

    plt.title("Graph Visualization with Zones and Detailed Connections")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper right", fontsize="small")
    plt.show()
