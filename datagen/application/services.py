from sqlalchemy import update

from application import modelers

from domain.models import Account

def account_register(session):
    new_account = modelers.random_account()
    session.add(new_account)
    new_address = modelers.random_address(new_account.id)
    session.add(new_address)

def send_alarm(session, account_id):
    new_alarm = modelers.random_alarm(account_id)
    session.add(new_alarm)

def family_account_register(session, account_ids):
    new_family_account = modelers.random_family_account(account_ids[0])
    session.add(new_family_account)
    session.execute(
        update(Account).where(Account.id.in_(account_ids)).values(family_account_id=new_family_account.id)
    )

def store_register(session):
    new_store = modelers.random_store()
    session.add(new_store)

def add_favorites(session, account_id, store_id):
    new_favorite = modelers.favorite(account_id, store_id)
    session.add(new_favorite)