from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo

class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    password = StringProperty(required=True)
    blocked = StringProperty(default="false")
    status = StringProperty(default="active")

    created_by = RelationshipTo('src.models.user_model.User', 'CREATED_BY')
    roles = RelationshipTo('src.models.role_model.Role', 'HAS_ROLE')
    capacities = RelationshipTo('src.models.capacity_model.Capacity', 'HAS_CAPACITY')
    sessions = RelationshipTo('src.models.session_model.Session', 'HAS_SESSION')
