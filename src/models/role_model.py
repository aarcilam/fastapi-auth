from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom

class Role(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    # Use fully-qualified path for User so neomodel resolves the reference
    # across modules rather than looking for User inside this module.
    users = RelationshipFrom('src.models.user_model.User', 'HAS_ROLE')
