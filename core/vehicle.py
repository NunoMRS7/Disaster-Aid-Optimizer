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

    def calculate_autonomy_loss(self, load: float) -> float:
        """
        Calculate the autonomy reduction based on the load carried.
        
        Args:
            load (float): Load in kilograms.
        
        Returns:
            float: Adjusted autonomy in kilometers.
        """
        result = self.autonomy - (load / self.capacity * self.autonomy)
        self.autonomy = result
        return result
