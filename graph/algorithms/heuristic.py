def heuristic(current_zone, goal_zone):
    """
    Heuristic function for Greedy Search based on zone properties and travel cost.

    Args:
        current_zone (Zone): The current zone in the graph.
        goal_zone (Zone): The destination zone.

    Returns:
        float: A heuristic estimate of the cost to reach the goal zone.
    """
    # Ensure that both current_zone and goal_zone are valid
    if current_zone is None or goal_zone is None:
        raise ValueError("Current zone and goal zone must be valid Zone instances.")
    
    severity_difference = abs(current_zone.severity.value - goal_zone.severity.value)

    population_difference = abs(current_zone.population - goal_zone.population)

    heuristic_value = severity_difference * 1.5 + population_difference * 0.5

    return heuristic_value
