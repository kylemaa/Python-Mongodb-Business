import mongoengine


class Ordering(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField()
    guest_snake_id = mongoengine.ObjectIdField()

    ordered_date = mongoengine.DateTimeField()
    delivered_date = mongoengine.DateTimeField()