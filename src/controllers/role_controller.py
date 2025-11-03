from src.services.role_service import RoleService

class RoleController:

    def create_role(self, name: str):
        roleService = RoleService()
        role = roleService.create_role(name=name)
        return role

    def get_roles(self):
        roleService = RoleService()
        roles = roleService.get_roles()
        return roles