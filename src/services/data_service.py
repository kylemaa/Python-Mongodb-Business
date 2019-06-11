import mongoengine
from typing import List
import data.owners as Owner
from data.orders import Ordering as Ordering
from data.shipments import Shipment
import bson


# Use mongoengine method .objects to match with object passed to this function.
# Return the first result of this Query or None with .first()
def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()
    return owner


def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.email = email
    owner.name = name

    owner.save()
    return owner


def find_shipments_for_user(account: Owner) -> List[Shipment]:
    query = Shipment.objects(id__in=account.shipment_ids)
    shipments = list(query)
    return shipments


def order_shipment(account, customer, item, amount):
    order: Ordering = None

    order.guest_owner_id = account.id
    order.guest_customer_id = customer.id
    order.guest_item_id = item.id
    order.guest_amount = amount

    Shipment.save()