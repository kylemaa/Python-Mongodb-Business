from src.data.owner import Owner
# Need to do/import service method as svc to find account by email
active_app_user: Owner = None
def reload_user_app():
    global active_app_user
    if not active_app_user:
        return
    else:
        active_app_user = svc.find_account_by_email(active_app_user.email)