from src.models.capacity_model import Capacity
from src.models.role_model import Role
from typing import List

class CapacityService:
    def create_capacity(self, name: str, description: str):
        capacity = Capacity(name=name, description=description).save()
        return capacity

    def get_capacities(self):
        capacities = Capacity.nodes.all()
        return capacities

    def get_capacities_with_id(self, uids: List[str]):
        capacities = Capacity.nodes.filter(uid__in=uids)
        return capacities

    def assing_capacity_to_user(self, role: Role, capacity: Capacity):
        role.capacities.connect(capacity)
        return True
    
    def get_capacity_by_name(self, name: str):
        try:
            capacity = Capacity.nodes.get(name=name)
            return capacity
        except Exception:
            return None