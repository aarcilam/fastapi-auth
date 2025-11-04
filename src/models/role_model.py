from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom, RelationshipTo

class Role(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    capacities = RelationshipTo('src.models.capacity_model.Capacity', 'HAS_CAPACITY')
    users = RelationshipFrom('src.models.user_model.User', 'HAS_ROLE')
