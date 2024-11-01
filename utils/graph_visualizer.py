import matplotlib.pyplot as plt
from graph.graph_builder import Graph
import random

class GraphVisualizer:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.pos = {}
        self.edges = []
        self.labels = {}
        self.visited = set()
        self.stack = []
        self._initialize_positions()
        self.fig, self.ax = plt.subplots()

    def _initialize_positions(self):
        for idx, (zone, connections) in enumerate(self.graph.graph.items()):
            self.pos[zone] = (random.uniform(0, 10), random.uniform(0, 10))
            self.labels[zone] = f"{zone.name}"
            for neighbor, cost in connections:
                self.edges.append((zone, neighbor, cost))

    def print_graph(graph: Graph):
        """
        Prints a textual representation of the graph showing nodes and their connections.

        Args:
        graph (Graph): The graph to print.
        """
        for zone, connections in graph.graph.items():
            print(f"Zone {zone.name} ({zone.severity}):")
            for neighbor, cost in connections:
                print(f"  -> Connected to {neighbor.name} with cost {cost:.2f} km")

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
            labels[zone] = f"{zone.name}"

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

    def visualize_step(self, node):
        """
        Visualize the current step of the algorithm.
        
        Args:
            node (Zone): The current node being visited.
        """
        self.visited.add(node)
        self.draw_graph()

    def draw_graph(self):
        self.ax.clear()  # Clear the current figure
        for node, (x, y) in self.pos.items():
            color = 'red' if node in self.visited else 'blue'
            self.ax.scatter(x, y, s=100, color=color)
            self.ax.text(x, y, self.labels[node], fontsize=12, ha='right')

        for start, end, cost in self.edges:
            x_values = [self.pos[start][0], self.pos[end][0]]
            y_values = [self.pos[start][1], self.pos[end][1]]
            self.ax.plot(x_values, y_values, 'b-', linewidth=1)
            mid_x, mid_y = (x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2
            self.ax.text(mid_x, mid_y, f"{cost:.2f}", color="red", fontsize=9)

        self.ax.set_title("Graph Visualization")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.fig.canvas.draw()  # Draw the updated figure
        plt.pause(0.1)  # Pause to allow interactive updates

    def set_stack(self, stack):
        """
        Set the current stack state for the DFS algorithm.
        
        Args:
            stack (list): The current stack state.
        """
        self.stack = stack