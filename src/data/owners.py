import mongoengine
import datetime


class Owner(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(require=True)
    email = mongoengine.StringField(require=True)

    customer_ids = mongoengine.StringField(required=True)
    shipment_ids = mongoengine.StringField(required=True)

    meta = {'dbalias': 'businessapp', 'collection': 'owners'}