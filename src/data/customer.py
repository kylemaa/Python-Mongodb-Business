import mongoengine
import datetime


class Customer:
    register_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    phone_number= mongoengine.StringField(required=True)

    type_of_product = mongoengine.StringField(required=True)
    order_product = mongoengine.FloatField(required=True)

    meta = {'dbalias': 'businessapp', 'collection': 'customer'}