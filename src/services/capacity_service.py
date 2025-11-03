from src.models.capacity_model import Capacity
from src.models.user_model import User

class CapacityService:
    def create_capacity(self, name: str, limit: int):
        capacity = Capacity(name=name, limit=limit).save()
        return capacity

    def get_capacities(self):
        capacities = Capacity.nodes.all()
        return capacities

    def get_capacities_with_id(self, uids: List[str]):
        capacities = Capacity.nodes.filter(uid__in=uids)
        return capacities

    def assing_capacity_to_user(self, user: User, capacity: Capacity):
        user.capacity.connect(capacity)
        return True