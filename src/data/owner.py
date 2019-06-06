class Owner:
    register_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(require=True)
    email = mongoengine.StringField(require=True)

    customer_ids = mongoengine.StringField(required=True)
    order_ids = mongoengine.StringField(required=True)

    meta = {'dbalias': 'businessapp', 'collection': 'customer'}