from src.services.capacity_service import CapacityService

class CapacityController:
    def get_capacities(self):
        capacity_service = CapacityService()
        capacities = capacity_service.get_capacities()
        return capacities

    def create_capacity(self, name: str, limit: int):
        capacity_service = CapacityService()
        capacity = capacity_service.create_capacity(name, limit)
        return capacity