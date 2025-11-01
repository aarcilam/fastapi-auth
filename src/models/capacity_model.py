from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom

class Capacity(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    description = StringProperty(required=False)

    user = RelationshipFrom('src.models.user_model.User', 'HAS_CAPACITY')