from core.zone import Zone

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
    
    def add_connection(self, zone1: Zone, zone2: Zone, cost: float):
        """
        Create a bi-directional edge between two zones with an associated cost.
        
        Args:
            zone1 (Zone): First zone.
            zone2 (Zone): Second zone.
            cost (float): The cost of traveling between the two zones.
        """
        self.add_zone(zone1)
        self.add_zone(zone2)
        self.graph[zone1].append((zone2, cost))
        self.graph[zone2].append((zone1, cost))
