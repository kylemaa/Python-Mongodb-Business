import data.owner as Owner
import bson


# Use mongoengine method .objects to match with object passed to this function.
# Return the first result of this Query or None with .first()
def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()


def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.email = email
    owner.name = name

    owner.save()
    return owner
