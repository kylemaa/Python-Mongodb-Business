from src.data.orders import Ordering as Ordering
import mongoengine
import datetime


class Shipment(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    name = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=True)

    orders = mongoengine.EmbeddedDocumentListField(Ordering)
    meta = {'dbalias': 'businessapp', 'collection': 'shipments'}
