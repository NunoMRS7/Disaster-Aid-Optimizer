import random
import time
import tracemalloc
import matplotlib.pyplot as plt

from core.vehicle import Vehicle
from enums.vehicle_type import VehicleType
from graph.algorithms.greedy import greedy
from graph.algorithms.a_star import a_star
from graph.algorithms.bfs import bfs
from graph.algorithms.dfs import dfs
from utils.graph_generator import apply_randomness_to_graph, generate_random_graph

def benchmark_algorithm(algorithm_func, graph, initial_state, goal_state, heuristic=True, vehicle=None):
    """
    Benchmarks a graph traversal algorithm, including metrics like execution time,
    memory usage, and path quality.
    
    :param algorithm_func: The algorithm function to benchmark.
    :param graph: The graph object to traverse.
    :param initial_state: The starting zone/state.
    :param goal_state: The target zone/state.
    :param heuristic: Optional heuristic function (for dynamic A*).
    :param vehicle: Optional vehicle object (for vehicle-specific algorithms).
    :return: A dictionary of performance metrics.
    """

    start_time = time.time()
    tracemalloc.start()

    if not heuristic and vehicle:
        path, visited_zones, total_cost = algorithm_func(graph, initial_state, goal_state, heuristic, vehicle)
    else:
        path, visited_zones, total_cost = algorithm_func(graph, initial_state, goal_state)

    end_time = time.time()
    _, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    total_zones = len(graph.get_all_zones())
    solution_length = len(path) - 1 if path else 0
    avg_cost_per_edge = total_cost / solution_length if solution_length > 0 else 0
    zones_visited_percentage = (len(visited_zones) / total_zones) * 100 if total_zones > 0 else 0

    metrics = {
        "execution_time": end_time - start_time,
        "peak_memory_usage": peak_memory / 1024,
        "zones_visited": len(visited_zones),
        "solution_depth": solution_length,
        "solution_cost": total_cost,
        "avg_cost_per_edge": avg_cost_per_edge,
        "zones_visited_percentage": zones_visited_percentage,
    }

    return metrics

def compare_algorithms(algorithms, graph, initial_state, goal_state):
    """
    Benchmarks multiple algorithms on a certain graph given a specific initial state and goal state.

    Args:
        algorithms (dict): Dictionary where keys are algorithm names (str) and values
                           are algorithm functions to benchmark.
        graph (object): The data structure representing the graph.
        initial_state (object): The starting point for the search.
        goal_state (object): The target point for the search.

    Returns:
        dict: A dictionary containing benchmark results for each algorithm.
              Each key corresponds to an algorithm name, and each value is a 
              dictionary of performance metrics as returned by `benchmark_algorithm`.
    """

    results = {}
    for name, algorithm in algorithms.items():
        metrics = benchmark_algorithm(algorithm, graph, initial_state, goal_state)
        results[name] = metrics

    return results

def bulk_benchmarking():
    """
    Performs bulk benchmarking on various algorithms over graphs of increasing size.
    Metrics are calculated for each graph size and saved for analysis.
    """
    import json

    graph_sizes = [5, 10, 20, 50, 100, 500]
    
    algorithms = {
        "DFS": dfs,
        "BFS": bfs,
        "A* Search": a_star,
        "Greedy": greedy,
        "Dynamic A* Search": a_star,
    }

    results = {}
    autonomyCapacity = 800

    for size in graph_sizes:
        print(f"Generating graph with {size} nodes...")
        graph = generate_random_graph(size)
        apply_randomness_to_graph(graph)

        zones = list(graph.get_all_zones())
        if len(zones) < 2:
            print(f"Graph with size {size} has insufficient zones. Skipping...")
            continue

        initial_zone = random.choice(zones)
        goal_zone = random.choice([z for z in zones if z != initial_zone])

        vehicle = Vehicle(VehicleType.TRUCK, autonomyCapacity, autonomyCapacity)
        autonomyCapacity = autonomyCapacity + 200

        print(f"Benchmarking algorithms on graph with {size} nodes...")
        results[size] = {}

        for name, algorithm in algorithms.items():
            print(f"Running {name}...")
            
            try:
                if name == "Dynamic A* Search":
                    metrics = benchmark_algorithm(algorithm, graph, initial_zone, goal_zone, False, vehicle)
                else:
                    metrics = benchmark_algorithm(algorithm, graph, initial_zone, goal_zone)
                results[size][name] = metrics
            except Exception as e:
                print(f"Error running {name}: {e}")
                results[size][name] = "No path found"

        print(f"Completed benchmarking for graph with {size} nodes.\n")

    with open("bulk_benchmarking_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Bulk benchmarking complete. Results saved to 'bulk_benchmarking_results.json'.")

def visualize_comparisons(data):
    metrics = [
        "execution_time",
        "peak_memory_usage",
        "zones_visited",
        "solution_depth",
        "solution_cost",
        "avg_cost_per_edge",
        "zones_visited_percentage"
    ]
    
    for metric in metrics:
        plt.figure(figsize=(12, 6))
        x_values = sorted(map(int, data.keys()))
        algorithms = list(data[str(x_values[0])].keys())
        
        for algorithm in algorithms:
            y_values = [
                data[str(x)][algorithm].get(metric, 0) for x in x_values
            ]
            plt.plot(x_values, y_values, marker='o', label=algorithm)
        
        plt.title(f'Comparison of {metric.replace("_", " ").capitalize()}')
        plt.xlabel('Number of Zones')
        plt.ylabel(metric.replace("_", " ").capitalize())
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
