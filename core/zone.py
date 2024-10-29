from enums.geography import GeographyType
from enums.rating import Rating
import string

class Zone:
    """
    Class representing a disaster-affected zone.
    
    Attributes:
        geography (GeographyType): The geographical type of the zone.
        severity (Rating): Priority based on severity of the situation.
        population (int): The population size within the zone.
    """

    def __init__(self, name: string, geography: GeographyType, severity: Rating, population: int):
        self.name = name
        self.geography = geography
        self.severity = severity
        self.population = population
