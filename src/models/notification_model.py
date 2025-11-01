from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipFrom

class Notification(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(required=True)
    message = StringProperty(required=True)

    user = RelationshipFrom('src.models.user_model.User', 'RECEIVES_NOTIFICATION')