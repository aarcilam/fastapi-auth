from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom

class Capacity(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    description = StringProperty(required=False)

    role = RelationshipFrom('src.models.role_model.Role', 'HAS_CAPACITY')