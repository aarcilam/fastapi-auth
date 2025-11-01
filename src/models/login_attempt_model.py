from neomodel import StructuredNode, StringProperty, UniqueIdProperty, DateTimeNeo4jFormatProperty

class LoginAttempt(StructuredNode):
    uid = UniqueIdProperty()
    timestamp = DateTimeNeo4jFormatProperty(default_now=True)
    ip_address = StringProperty(required=True)