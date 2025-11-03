from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo

class Notification(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(required=True)
    message = StringProperty(required=True)

    user = RelationshipTo('src.models.user_model.User', 'RECEIVES_NOTIFICATION')