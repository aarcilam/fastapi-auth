from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class LoginAttempt(StructuredNode):
    uid = UniqueIdProperty()
    timestamp = StringProperty(required=True)
    ip_address = StringProperty(required=True)