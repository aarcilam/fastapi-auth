from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo, JSONProperty, DateTimeNeo4jFormatProperty, BooleanProperty

class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    phone = StringProperty(unique_index=True, required=False)
    password = StringProperty(required=True)
    blocked = BooleanProperty(default=False)    
    status = StringProperty(default="active")
    metadata = JSONProperty(default={})
    created_at = DateTimeNeo4jFormatProperty(default_now=True)

    created_by = RelationshipTo('src.models.user_model.User', 'CREATED_BY')
    roles = RelationshipTo('src.models.role_model.Role', 'HAS_ROLE')
    capacities = RelationshipTo('src.models.capacity_model.Capacity', 'HAS_CAPACITY')
    sessions = RelationshipTo('src.models.session_model.Session', 'HAS_SESSION')
    notifications = RelationshipTo('src.models.notification_model.Notification', 'RECEIVES_NOTIFICATION')
