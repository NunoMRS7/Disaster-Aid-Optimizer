import math

class Coordinate:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def calculate_distance(self, other):
        """
        Calculates the distance between two geographical coordinates.
        
        Args:
            other (Coordinate): The other geographical coordinate.
        
        Returns:
            float: The distance between the two coordinates.
        """
        # Haversine formula to calculate distance between two points on Earth
        R = 6371
        lat1 = self.latitude
        lon1 = self.longitude
        lat2 = other.latitude
        lon2 = other.longitude

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c
