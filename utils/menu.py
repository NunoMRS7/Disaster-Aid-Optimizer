from core.vehicle import Vehicle
from graph.algorithms.bfs import bfs
from graph.algorithms.dfs import dfs
from graph.algorithms.a_star import a_star
from enums.vehicle_type import VehicleType
from utils.graph_generator import generate_random_graph, apply_randomness_to_graph, generate_map_graph
from utils.graph_visualizer import print_graph, visualize_graph
from map.src.plot_portugal_graph import visualize_generated_graph


class Menu:
    def __init__(self):
        self.drone = Vehicle(VehicleType.DRONE, autonomy=500.0, capacity=10.0)
        self.graph = None
        self.is_portugal_map = False

    def display_main_menu(self):
        print("\nMain Menu:")
        print("1. Generate a new random graph")
        print("2. Generate the map of Portugal")
        if self.graph is not None:
            print("3. Operate with the graph")
        print("0. Exit")

    def display_graph_menu(self):
        print("\nGraph Menu:")
        print("1. Print the current graph")
        print("2. Visualize the current graph")
        print("3. Calculate drone autonomy")
        print("4. Traverse the graph using DFS")
        print("5. Traverse the graph using BFS")
        print("6. Traverse the graph using A* Search")
        print("7. Traverse the graph using Weighted A* Search on a dynamic map")
        print("0. Back to Main Menu")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                input_nodes = input("Enter the number of nodes for the graph: ")
                self.graph = generate_random_graph(int(input_nodes))
                apply_randomness_to_graph(self.graph)
                self.is_portugal_map = False
                print("New random graph generated.")
            elif choice == '2':
                self.graph = generate_map_graph()
                apply_randomness_to_graph(self.graph)
                self.is_portugal_map = True
                print("Map of Portugal graph generated.")
            elif choice == '3' and self.graph is not None:
                self.run_graph_menu()
            elif choice == '0':
                print("Exiting the program...")
                break
            else:
                print("Invalid option. Please try again.")

    def run_graph_menu(self):
        while True:
            self.display_graph_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                if self.graph is not None:
                    print("Printing the graph:")
                    print_graph(self.graph)
                else:
                    print("Please generate a graph first.")
            elif choice == '2':
                if self.graph is not None:
                    print("Visualizing the graph:")
                    if self.is_portugal_map:
                        show_labels = input("Show labels (y/n)? ").lower() == 'y'
                        show_conditions = input("Show conditions (y/n)? ").lower() == 'y'
                        show_geography = input("Show geography (y/n)? ").lower() == 'y'
                        show_infrastructure = input("Show infrastructure (y/n)? ").lower() == 'y'
                        show_cost = input("Show cost (y/n)? ").lower() == 'y'
                        visualize_generated_graph(self.graph, show_labels, show_conditions, show_geography, show_infrastructure, show_cost)
                    else:
                        visualize_graph(self.graph)
                else:
                    print("Please generate a graph first.")
            elif choice == '3':
                if self.graph is not None:
                    print("Drone autonomy before carrying 5kg:", self.drone.autonomy)
                    print("Drone autonomy after carrying 5kg:", self.drone.calculate_autonomy_loss(5.0))
                else:
                    print("Please generate a graph first.")
            elif choice in ['4', '5', '6', '7']:
                if self.graph is not None:
                    start_zone_name = input("Enter the start zone: ")
                    start_zone = self.graph.get_zone(start_zone_name)
                    if start_zone is None:
                        print("Invalid start zone.")
                        continue

                    goal_zone_name = input("Enter the goal zone: ")
                    goal_zone = self.graph.get_zone(goal_zone_name)
                    if goal_zone is None:
                        print("Invalid goal zone.")
                        continue

                    if choice == '4':
                        best_path, visited, best_cost = dfs(self.graph, start_zone, goal_zone)
                        print("Algorithm: DFS")
                    elif choice == '5':
                        best_path, visited, best_cost = bfs(self.graph, start_zone, goal_zone)
                        print("Algorithm: BFS")
                    elif choice == '6':
                        best_path, visited, best_cost = a_star(self.graph, start_zone, goal_zone, True)
                        print("Algorithm: A* Search")
                    elif choice == '7':
                        best_path, visited, best_cost = a_star(self.graph, start_zone, goal_zone, False)
                        print("Algorithm: A* Search (Weighted)")

                    if best_path is None:
                        print("No path found.")
                    else:
                        print("Start zone:", start_zone.name)
                        print("Goal zone:", goal_zone.name)
                        print("Best path:", [zone.name for zone in best_path])
                        print("Visited zones:", [zone.name for zone in visited])
                        print("Best cost:", best_cost)
                else:
                    print("Please generate a graph first.")
            elif choice == '0':
                break
            else:
                print("Invalid option. Please try again.")
