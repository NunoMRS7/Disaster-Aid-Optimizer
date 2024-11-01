from core.vehicle import Vehicle
from graph.algorithms.bfs import bfs
from graph.algorithms.dfs import dfs
from graph.algorithms.a_star import a_star
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
        print("5. Traverse the graph using DFS")
        print("6. Traverse the graph using BFS")
        print("7. Traverse the graph using A* Search")
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

            elif choice in ['5', '6', '7']:
                if self.random_graph is not None:
                    
                    start_zone = self.random_graph.get_zone("C")
                    goal_zone = self.random_graph.get_zone("A")

                    if choice == '5':
                        best_path, visited, max_depth, best_cost = dfs(self.random_graph, start_zone, self.drone)
                        print("Algortihm: DFS")
                    elif choice == '6':
                        best_path, visited, max_depth, best_cost = bfs(self.random_graph, start_zone, goal_zone)
                        print("Algortihm: BFS")
                    elif choice == '7':
                        best_path, visited, max_depth, best_cost = a_star(self.random_graph, start_zone, goal_zone)
                        print("Algortihm: A* Search")

                    if best_path is None:
                        print("No path found.")
                    else:
                        print("Start zone:", start_zone.name)
                        print("Goal zone:", goal_zone.name)
                        print("Best path:", [zone.name for zone in best_path])
                        print("Visited zones:", [zone.name for zone in visited])
                        print("Max depth:", max_depth)
                        print("Best cost:", best_cost)
                else:
                    print("Please generate a graph first.")

            elif choice == '0':
                print("Exiting the program...")
                break

            else:
                print("Invalid option. Please try again.")
