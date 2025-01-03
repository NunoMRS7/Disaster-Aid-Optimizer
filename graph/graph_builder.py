from core.zone import Zone
import core.road as Road

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
    
    def add_connection(self, zone1: Zone, zone2: Zone, road: Road):
        """
        Create a bidirectional connection between two zones with a cost, weather conditions, geography, infrastructure, and availability.
        
        Args:
            zone1 (Zone): First zone.
            zone2 (Zone): Second zone.
            road (Road): Road object representing the connection between the two zones
        """
        self.add_zone(zone1)
        self.add_zone(zone2)
        
        self.graph[zone1].append((zone2, road))
        self.graph[zone2].append((zone1, road))

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

    def get_connections(self, zone: Zone):
        """
        Get all neighboring zones and their travel cost from the given zone.
        
        Args:
            zone (Zone): The zone from which to get neighbors.
        
        Returns:
            list of tuples: Each tuple contains a neighboring zone and the road object.
        """
        return [(neighbor, road) for neighbor, road in self.graph[zone]]
    
    def has_connection(self, zone1, zone2):
        """
        Check if there is a connection between two zones.

        Args:
            zone1 (Zone): First zone.
            zone2 (Zone): Second zone.

        Returns:
            bool: True if there is a connection, False otherwise.
        """
        return any(neighbor == zone2 for neighbor, _ in self.graph.get(zone1, []))

    def get_all_zones(self):
        """
        Get all zones in the graph.
        
        Returns:
            list: All zones in the graph.
        """
        return list(self.graph.keys())
