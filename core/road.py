class Road:
    """
    Class to represent a road in the simulation.

    Attributes:
        cost (float): The cost of traveling on the road.
        conditions (Conditions): The weather conditions on the road.
        geography (Geography): The geographical features of the road.
        infrastructure (Infrastructure): The infrastructure of the road.
        availability (bool): The availability of the road.
    """

    def __init__(self, cost=0, conditions=None, geography=None, infrastructure=None, availability=True):
        self.cost = cost
        self.conditions = conditions
        self.geography = geography
        self.infrastructure = infrastructure
        self.availability = availability
