from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo

class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    password = StringProperty(required=True)

    created_by = RelationshipTo('User', 'CREATED_BY')
    # Use fully-qualified path for Role so neomodel can resolve the class
    # across modules (avoids AttributeError when resolving by name).
    roles = RelationshipTo('src.models.role_model.Role', 'HAS_ROLE')
