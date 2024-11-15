from enums.conditions import Conditions
from enums.infrastructure import Infrastructure
from enums.geography import Geography

def edge_heuristic(cost, conditions, infrastructure, geography, availability):
    """
    Computes a heuristic score between two zones based on edge properties.

    Args:
        cost (float): The cost associated with the edge.
        conditions (Conditions): Conditions of the edge.
        infrastructure (Infrastructure): Infrastructure type of the edge.
        geography (Geography): Geography type of the edge.
        availability (bool): Availability of the edge.

    Returns:
        float: Heuristic score between the two zones, or float('inf') if unavailable.
    """
    # If the connection is not available, return infinity to avoid this edge
    if not availability:
        return float('inf')

    # Normalize and weigh edge components based on Conditions
    condition_weight = {
        Conditions.VERY_GOOD: 0.8,
        Conditions.GOOD: 1.0,
        Conditions.REASONABLE: 1.2,
        Conditions.BAD: 1.5,
        Conditions.VERY_BAD: 2.0,
    }
    
    infrastructure_weight = 0.8 if infrastructure == Infrastructure.HIGHWAY else 1.2  # Favor high-quality infrastructure
    
    # Geography weight
    geography_weight = 1.0  # Default weight
    if geography == Geography.MOUNTAINOUS:
        geography_weight = 1.5  # Penalize mountainous terrain
    elif geography == Geography.PLATEAU:
        geography_weight = 0.9  # Favor plateau terrain

    # Combine the weights with cost to produce the heuristic score
    edge_score = cost * condition_weight[conditions] * infrastructure_weight * geography_weight
    return edge_score
