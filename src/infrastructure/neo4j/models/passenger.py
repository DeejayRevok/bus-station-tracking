from neomodel import RelationshipTo, StringProperty, StructuredNode, ZeroOrOne


class Passenger(StructuredNode):
    passenger_id = StringProperty(unique_index=True, required=True)
    name = StringProperty(required=True)
    type = StringProperty(required=True)

    root_passenger = RelationshipTo("Passenger", "IS_TRIGGERED_BY", cardinality=ZeroOrOne)

    @classmethod
    def category(cls):
        cls.category()
