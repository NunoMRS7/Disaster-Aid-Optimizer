from core.vehicle import Vehicle
from graph.algorithms.bfs import bfs
from graph.algorithms.dfs import dfs
from graph.algorithms.a_star import a_star
from graph.algorithms.greedy import greedy
from enums.vehicle_type import VehicleType
from utils.graph_generator import generate_random_graph, apply_randomness_to_graph, generate_map_graph
from utils.graph_visualizer import print_graph, visualize_graph
from map.src.plot_portugal_graph import visualize_generated_graph
from metrics.metrics import benchmark_algorithm, bulk_benchmarking, visualize_comparisons
import json

class Menu:
    def __init__(self):
        self.vehicle = Vehicle(VehicleType.DRONE, autonomy=500, capacity=200)
        self.graph = None
        self.is_portugal_map = False
        self.has_benchmark_run = False

    def display_main_menu(self):
        print("\nMain Menu:")
        print("1. Generate a new random graph")
        print("2. Generate the map of Portugal")
        if self.graph is not None:
            print("3. Operate with the graph")
            print("4. Metrics")
        print("0. Exit")

    def display_graph_menu(self):
        print("\nGraph Menu:")
        print("1. Print the current graph")
        print("2. Visualize the current graph")
        print("3. Calculate vehicle autonomy")
        print("4. Traverse the graph using DFS")
        print("5. Traverse the graph using BFS")
        print("6. Traverse the graph using A* Search")
        print("7. Traverse the graph using Greedy Search")
        print("8. Traverse the graph using Weighted A* Search on a dynamic map")
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
            elif choice == '4' and self.graph is not None:
                self.run_metrics_menu()
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
                    print("Vehicle autonomy before carrying 5kg:", self.vehicle.autonomy)
                    print("Vehicle autonomy after carrying 5kg:", self.vehicle.calculate_autonomy_loss(5.0))
                else:
                    print("Please generate a graph first.")
            elif choice in ['4', '5', '6', '7', '8']:
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
                        best_path, visited, best_cost = greedy(self.graph, start_zone, goal_zone)
                        print("Algorithm: Greedy Search")
                    elif choice == '8':
                        vehicle_type = input("Enter the vehicle type (drone, car, truck): ").lower()
                        if vehicle_type == 'drone':
                            self.vehicle = Vehicle(VehicleType.DRONE, autonomy=40, capacity=20)
                        elif vehicle_type == 'car':
                            self.vehicle = Vehicle(VehicleType.CAR, autonomy=500, capacity=200)
                        elif vehicle_type == 'truck':
                            self.vehicle = Vehicle(VehicleType.TRUCK, autonomy=800, capacity=800)
                        else:
                            print("Invalid vehicle type.")
                            continue

                        best_path, visited, best_cost = a_star(self.graph, start_zone, goal_zone, False, self.vehicle)
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

    def metrics_menu(self):
        print("\nMetrics Menu:")
        print("1. Execute metrics on the algorithms")
        print("2. Execute bulk benchmarking")
        if self.has_benchmark_run:
            print("3. Show benchmarking results")
        print("0. Back to Main Menu")

    def run_metrics_menu(self):
        while True:
            self.metrics_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                print("Executing metrics on the algorithms...")
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

                    algorithms = {
                        "DFS": dfs,
                        "BFS": bfs,
                        "A* Search": a_star,
                        "Dynamic A* Search": a_star,
                    }

                    metrics = {}
                    for name, algorithm in algorithms.items():
                        if name == "Dynamic A* Search":
                            vehicle_type = input("Enter the vehicle type (drone, car, truck): ").lower()
                            if vehicle_type == 'drone':
                                self.vehicle = Vehicle(VehicleType.DRONE, autonomy=40, capacity=20)
                            elif vehicle_type == 'car':
                                self.vehicle = Vehicle(VehicleType.CAR, autonomy=500, capacity=200)
                            elif vehicle_type == 'truck':
                                self.vehicle = Vehicle(VehicleType.TRUCK, autonomy=800, capacity=800)
                            else:
                                print("Invalid vehicle type.")
                                continue

                            metrics[name] = benchmark_algorithm(algorithm, self.graph, start_zone, goal_zone, False, self.vehicle)
                        else:
                            metrics[name] = benchmark_algorithm(algorithm, self.graph, start_zone, goal_zone)
                    
                    for name, metric in metrics.items():
                        print(f"\n{name} metrics:")
                        for key, value in metric.items():
                            print(f"{key}: {value}")
                else:
                    print("Please generate a graph first.")
            elif choice == '2':
                print("Executing bulk benchmarking...")
                bulk_benchmarking()
                self.has_benchmark_run = True
            elif choice == '3' and self.has_benchmark_run:
                intention = input("Do you want to use the file \"bulk_benchmarking_results.json\" see the results? (y/n): ").lower()
                if intention == 'y':
                    with open("bulk_benchmarking_results.json", "r") as file:
                        results = json.load(file)
                        visualize_comparisons(results)
                else:
                    filePath = input("Enter the file path: ")
                    with open(filePath, "r") as file:
                        results = json.load(file)
                        visualize_comparisons(results)
            elif choice == '0':
                break
            else:
                print("Invalid option. Please try again.")
