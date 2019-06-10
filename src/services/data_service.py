import data.owners as Owner
from data.orders import Ordering as Ordering
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


def order_item(account, customer, item, amount):
    order: Ordering = None

    order.guest_owner_id = account.id
    order.guest_customer_id = customer.id
    order.guest_item_id = item.id
    order.guest_amount = amount

    shipment.save