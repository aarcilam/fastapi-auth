from src.services.capacity_service import CapacityService   

class SeedCapacities:
    def run(self):
        capacities : list[dict] = [
            {"name": "CREATE_USER", "description": "Capacity to create users"},
            {"name": "DELETE_USER", "description": "Capacity to delete users"},
            {"name": "UPDATE_USER", "description": "Capacity to update users"},
            {"name": "VIEW_USER", "description": "Capacity to view users"},
            {"name": "CREATE_ROLE", "description": "Capacity to create roles"},
            {"name": "DELETE_ROLE", "description": "Capacity to delete roles"},
            {"name": "UPDATE_ROLE", "description": "Capacity to update roles"},
            {"name": "VIEW_ROLE", "description": "Capacity to view roles"},
        ]

        for capacity_data in capacities:
            capacity_service = CapacityService()
            try:
                existing_capacity = capacity_service.get_capacity_by_name(capacity_data["name"])
            except Exception:
                existing_capacity = None
            if not existing_capacity:
                capacity_service.create_capacity(
                    name=capacity_data["name"],
                    description=capacity_data["description"]
                )