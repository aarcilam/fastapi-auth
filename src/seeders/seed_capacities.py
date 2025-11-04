from src.services.capacity_service import CapacityService   
from src.services.role_service import RoleService

class SeedCapacities:
    def run(self):
        capacities : list[dict] = [
            {"name": "CREATE_USER", "description": "Capacity to create users", "role": "admin"},
            {"name": "DELETE_USER", "description": "Capacity to delete users", "role": "admin"},
            {"name": "UPDATE_USER", "description": "Capacity to update users", "role": "admin"},
            {"name": "VIEW_USER", "description": "Capacity to view users", "role": "admin"},
            {"name": "CREATE_ROLE", "description": "Capacity to create roles", "role": "admin"},
            {"name": "DELETE_ROLE", "description": "Capacity to delete roles", "role": "admin"},
            {"name": "UPDATE_ROLE", "description": "Capacity to update roles", "role": "admin"},
            {"name": "VIEW_ROLE", "description": "Capacity to view roles", "role": "admin"},
        ]

        for capacity_data in capacities:
            capacity_service = CapacityService()
            role_service = RoleService()
            try:
                existing_capacity = capacity_service.get_capacity_by_name(capacity_data["name"])
            except Exception:
                existing_capacity = None
            if not existing_capacity:
                capacity = capacity_service.create_capacity(
                    name=capacity_data["name"],
                    description=capacity_data["description"]
                )
                role = role_service.get_role_or_create(capacity_data["role"])
                capacity_service.assing_capacity_to_user(role=role, capacity=capacity)
                print(f"Created capacity: {capacity.name} and assigned to role: {role.name}")
