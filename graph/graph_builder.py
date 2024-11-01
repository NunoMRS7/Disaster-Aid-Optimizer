from core.zone import Zone
from enums.conditions import Conditions
from enums.geography import Geography
from enums.infrastructure import Infrastructure

class Graph:
    """
    Class representing a basic undirected graph of zones with edge costs.
    """
    
    def __init__(self):
        self.graph = {}
    
    def add_zone(self, zone: Zone):
        """
        Add a zone as a node in the graph.
        
        Args:
            zone (Zone): Zone object to add.
        """
        if zone not in self.graph:
            self.graph[zone] = []
    
    def add_connection(self, zone1: Zone, zone2: Zone, cost: float, conditions: Conditions, geography: Geography, infrastructure: Infrastructure, availability: bool):
        """
        Create a bidirectional connection between two zones with a cost, weather conditions, geography, infrastructure, and availability.
        
        Args:
            zone1 (Zone): First zone.
            zone2 (Zone): Second zone.
            cost (float): The cost of traveling between the two zones.
            conditions (Conditions): The weather conditions between the two zones.
            geography (Geography): The geographical features between the two zones.
            infrastructure (Infrastructure): The infrastructure between the two zones.
            availability (bool): The availability of the connection.
        """
        self.add_zone(zone1)
        self.add_zone(zone2)
        self.graph[zone1].append((zone2, cost, conditions, geography, infrastructure, availability))
        self.graph[zone2].append((zone1, cost, conditions, geography, infrastructure, availability))

    def get_zone(self, name: str):
        """
        Get the zone object by its name.
        
        Args:
            name (str): The name of the zone.
        
        Returns:
            Zone: The zone object.
        """
        for zone in self.graph:
            if zone.name == name:
                return zone
