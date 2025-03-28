from utils.coordinate import Coordinate
from enums.severity import Severity
import string

class Zone:
    """
    Class representing a disaster-affected zone.
    
    Attributes:
        name (string): The name of the zone.
        coordinate (Coordinate): The geographical coordinate of the zone.
        severity (Severity): Priority based on severity of the situation.
        population (int): The population size within the zone.
        distanceToGoal (float): The distance to the goal zone.
        heuristic (float): The heuristic value of the zone.
        supplies (int): The amount of supplies available in the zone.
    """

    def __init__(self, name: string="", coordinate: Coordinate=Coordinate(), severity: Severity=3, population: int=0):
        self.name = name
        self.coordinate = coordinate
        self.severity = severity
        self.population = population
        self.distanceToGoal = -1
        self.heuristic = -1
        self.supplies = 0

    def determine_self_heuristic(self):
        """
        Determines the heuristic value of the zone based on its properties.
        """
        # Escalate the severity and population to a common scale
        severity_weight = 0.7 
        population_weight = 0.3

        scaled_severity = self.severity / 6
        scaled_population = (self.population - 1000) / (100000 - 1000)

        # Calculate the heuristic value
        self.heuristic = severity_weight * scaled_severity + population_weight * scaled_population

    def determine_self_distance_to_goal(self, goal_zone):
        """
        Determines the distance to the goal zone.
        
        Args:
            goal_zone (Zone): The goal zone.
        """
        self.distanceToGoal = self.coordinate.calculate_distance(goal_zone.coordinate)

    def calculate_distance_between_zones(self, other_zone):
        """
        Calculates the distance between two zones.
        
        Args:
            other_zone (Zone): The other zone.
        
        Returns:
            float: The distance between the two zones.
        """
        return self.coordinate.calculate_distance(other_zone.coordinate)
    
    def calculate_supplies_to_leave(self):
        """
        Calculate the amount of supplies to leave at a zone based on its properties.

        Args:
            zone (Zone): The zone to leave supplies at.

        Returns:
            float: The amount of supplies to leave.
        """
        severity_weight = 0.7
        population_weight = 0.3

        scaled_severity = self.severity / 6
        scaled_population = (self.population - 1000) / (100000 - 1000)

        return severity_weight * scaled_severity + population_weight * scaled_population * 100  # Scale to kg