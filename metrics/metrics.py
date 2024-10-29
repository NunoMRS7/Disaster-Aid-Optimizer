import time
import tracemalloc


def benchmark_algorithm(algorithm_func, graph, initial_state, goal_state):
    """
    Measures the performance of a search algorithm applied to a graph, given a specific initial state and goal state.

    Args:
        algorithm_func (function): The search algorithm function to be benchmarked.
                                   Should accept parameters (graph, initial_state, goal_state) 
                                   and return (nodes_visited, depth, solution_cost).
        graph (object): The data structure representing the graph.
        initial_state (object): The starting point for the search.
        goal_state (object): The target point for the search.

    Returns:
        dict: A dictionary containing the following metrics:
              - "execution_time": Total time taken by the algorithm (in seconds).
              - "peak_memory_usage": Maximum memory usage (in KB).
              - "nodes_visited": Total nodes visited by the algorithm.
              - "solution_depth": Depth of the solution path.
              - "solution_cost": Cost associated with the solution path.
    """

    
    # Start the clock and memory tracking
    start_time = time.time()
    tracemalloc.start()
    
    # Execute the algorithm and collect its result metrics
    nodes_visited, depth, solution_cost = algorithm_func(graph, initial_state, goal_state)
    
    # Stop the clock and measure peak memory usage
    end_time = time.time()
    _, peak_memory = tracemalloc.get_traced_memory()

    # stop the memory tracking
    tracemalloc.stop()
    
    # Prepare the metrics dictionary
    metrics = {
        "execution_time": end_time - start_time,   
        "peak_memory_usage": peak_memory / 1024,   
        "nodes_visited": nodes_visited,           
        "solution_depth": depth,                   
        "solution_cost": solution_cost             
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
        # Benchmark the current algorithm
        metrics = benchmark_algorithm(algorithm, graph, initial_state, goal_state)
        results[name] = metrics

    return results