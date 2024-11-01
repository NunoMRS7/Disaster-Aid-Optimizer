from core.vehicle import Vehicle
from graph.algorithms.dfs_with_interrupt import dfs_with_interrupt
from enums.vehicle_type import VehicleType
from utils.graph_generator import generate_random_graph
from utils.graph_visualizer import GraphVisualizer

def display_menu():
    print("\nMenu:")
    print("1. Generate a new graph")
    print("2. Print the current graph")
    print("3. Visualize the current graph")
    print("4. Calculate drone autonomy")
    print("5. Traverse the graph using DFS with interrupt (drone autonomy)")
    print("6. Visualize the DFS algorithm step by step")
    print("0. Exit")

def main():
    drone = Vehicle(VehicleType.DRONE, autonomy=500.0, capacity=10)
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            # Generate a new graph with the quantity of nodes chosen by the user
            input_nodes = input("Enter the number of nodes for the graph: ")
            random_graph = generate_random_graph(int(input_nodes)) 
            print("New graph generated.")

        elif choice == '2':
            # Check if the graph has been generated
            if random_graph is not None:
                print("Printing the graph:")
                GraphVisualizer.print_graph(random_graph)
            else:
                print("Please generate a graph first.")

        elif choice == '3':
            # Check if the graph has been generated
            if random_graph is not None:
                print("Visualizing the graph:")
                GraphVisualizer.visualize_graph(random_graph)
            else:
                print("Please generate a graph first.")

        elif choice == '4':
            # Calculate and display drone autonomy
            if random_graph is not None:
                print("Drone autonomy before carrying 5kg:", drone.autonomy)
                print("Drone autonomy after carrying 5kg:", drone.calculate_autonomy_loss(5.0))
            else:
                print("Please generate a graph first.")

        elif choice == '5':
            # Check if the graph has been generated
            if random_graph is not None:
                # Select a start zone from the generated graph
                start_zone = next(iter(random_graph.graph))  # Select an arbitrary start zone

                # Traverse the graph using a depth-first search algorithm
                visited_zones = dfs_with_interrupt(random_graph, start_zone, drone)
                print("\nZones visited in order:")
                for zone in visited_zones:
                    print(zone.geography, "-", zone.severity)
            else:
                print("Please generate a graph first.")
        elif choice == "6":
            if random_graph is not None:
                visualizer = GraphVisualizer(random_graph)
                dfs_with_interrupt(random_graph, list(random_graph.graph.keys())[0], drone, visualizer)
            else:
                print("No graph available. Generate a graph first.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()