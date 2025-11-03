from src.models.role_model import Role

class RoleService:
    def get_role_or_create(self, name: str):
        try:
            role = Role.nodes.get(name=name)
            if not role:
                role = Role(name=name).save()
            return role
        except Exception:
            role = Role(name=name).save()
            return role

    def create_role(self, name: str):
        role = Role(name=name).save()
        return role

    def get_roles(self):
        roles = Role.nodes.all()
        return roles

    def get_role(self, name: str):
        try:
            role = Role.nodes.get(name=name)
            return role
        except Exception:
            return None

