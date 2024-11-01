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
    print("5. Visualize the DFS algorithm step by step")
    print("0. Exit")

def main():
    graph = None
    vehicle = Vehicle(VehicleType.DRONE, autonomy=100.0, capacity=10)
    visualizer = None
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num_nodes = int(input("Enter the number of nodes: "))
            graph = generate_random_graph(num_nodes)
            print("Graph generated.")
        elif choice == "2":
            if graph:
                GraphVisualizer.print_graph(graph)
            else:
                print("No graph available. Generate a graph first.")
        elif choice == "3":
            if graph:
                GraphVisualizer.visualize_graph(graph)
            else:
                print("No graph available. Generate a graph first.")
        elif choice == "4":
            print(f"Vehicle autonomy: {vehicle.autonomy} km")
        elif choice == "5":
            if graph:
                visualizer = GraphVisualizer(graph)
                dfs_with_interrupt(graph, list(graph.graph.keys())[0], vehicle, visualizer)
            else:
                print("No graph available. Generate a graph first.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()