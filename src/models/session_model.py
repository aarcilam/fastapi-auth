from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom, DateTimeNeo4jFormatProperty

class Session(StructuredNode):
    uid = UniqueIdProperty()
    token = StringProperty(required=True)
    created_at = DateTimeNeo4jFormatProperty(default_now=True)

    user = RelationshipFrom('src.models.user_model.User', 'HAS_SESSION')