from core.vehicle import Vehicle
from graph.algorithms.dfs_with_interrupt import dfs_with_interrupt
from graph.algorithms.bfs_base import bfs
from graph.algorithms.dfs_base import dfs
from graph.algorithms.greedy_base import greedy_search
from graph.algorithms.a_star_base import a_star
from graph.algorithms.heuristic import heuristic
from enums.vehicle_type import VehicleType
from utils.graph_generator import generate_random_graph
from utils.graph_visualizer import print_graph, visualize_graph

class Menu:
    def __init__(self):
        self.drone = Vehicle(VehicleType.DRONE, autonomy=500.0, capacity=10.0)
        self.random_graph = None

    def display_menu(self):
        print("\nMenu:")
        print("1. Generate a new graph")
        print("2. Print the current graph")
        print("3. Visualize the current graph")
        print("4. Calculate drone autonomy")
        print("5. Traverse the graph using DFS with interrupt (drone autonomy)")
        print("6. Traverse the graph using DFS")
        print("7. Traverse the graph using BFS")
        print("8. Traverse the graph using Greedy Search")
        print("9. Traverse the graph using A* Search")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                input_nodes = input("Enter the number of nodes for the graph: ")
                self.random_graph = generate_random_graph(int(input_nodes))
                print("New graph generated.")

            elif choice == '2':
                if self.random_graph is not None:
                    print("Printing the graph:")
                    print_graph(self.random_graph)
                else:
                    print("Please generate a graph first.")

            elif choice == '3':
                if self.random_graph is not None:
                    print("Visualizing the graph:")
                    visualize_graph(self.random_graph)
                else:
                    print("Please generate a graph first.")

            elif choice == '4':
                if self.random_graph is not None:
                    print("Drone autonomy before carrying 5kg:", self.drone.autonomy)
                    print("Drone autonomy after carrying 5kg:", self.drone.calculate_autonomy_loss(5.0))
                else:
                    print("Please generate a graph first.")

            elif choice in ['5', '6', '7', '8', '9']:
                if self.random_graph is not None:
                    start_zone = next(iter(self.random_graph.graph))  # Select an arbitrary start zone
                    goal_zone = next(iter(self.random_graph.graph))  # Select an arbitrary end zone
                    
                    if start_zone == goal_zone:
                        goal_zone = next(iter(self.random_graph.graph)) # Ensure start and goal zones are different

                    if choice == '5':
                        visited_zones, _, _ = dfs_with_interrupt(self.random_graph, start_zone, self.drone)
                    elif choice == '6':
                        visited_zones, _, _ = dfs(self.random_graph, start_zone, goal_zone)
                    elif choice == '7':
                        visited_zones, _, _ = bfs(self.random_graph, start_zone, goal_zone)
                    elif choice == '8':
                        visited_zones, _, _ = greedy_search(self.random_graph, start_zone, goal_zone, heuristic)
                    elif choice == '9':
                        visited_zones, _, _ = a_star(self.random_graph, start_zone, goal_zone, heuristic)

                    print("\nZones visited in order:")
                    for zone in visited_zones:
                        print(zone.name, "-", zone.severity)
                else:
                    print("Please generate a graph first.")

            elif choice == '0':
                print("Exiting the program...")
                break

            else:
                print("Invalid option. Please try again.")
