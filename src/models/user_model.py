from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
    password = StringProperty(required=True)
