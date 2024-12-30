from enums.vehicle_type import VehicleType

class Vehicle:
    """
    Class representing a vehicle used in resource distribution during disaster relief.
    
    Attributes:
        type (VehicleType): The type of the vehicle, such as drone, car, or truck.
        autonomy (float): The autonomy of the vehicle in kilometers.
        capacity (float): The load capacity of the vehicle in kilograms.
    """

    def __init__(self, vehicle_type: VehicleType, autonomy: float, capacity: float):
        self.type = vehicle_type
        self.autonomy = autonomy
        self.capacity = capacity
        self.load = capacity

    def calculate_autonomy_loss(self, distance):
        """
        Calculate the autonomy reduction based on the load carried and distance traveled.
        
        Args:
            distance (float): The distance traveled in kilometers
        """
        return (distance * (1 + (self.load / self.capacity) * 0.5))
