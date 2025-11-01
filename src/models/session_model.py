from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom

class Session(StructuredNode):
    uid = UniqueIdProperty()
    token = StringProperty(required=True)
    created_at = StringProperty(required=True)

    user = RelationshipFrom('src.models.user_model.User', 'HAS_SESSION')