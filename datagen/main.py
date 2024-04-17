import json

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from application import service
from application import randomizer

from domain.models import Account, Address, Store

# create an engine to connect to a database
with open('conf.json') as f:
    config = json.load(f)
engine = create_engine(config['url'])

# create a session factory
Session = sessionmaker(bind=engine)

# create a base class for our model classes
Base = declarative_base()
Base.metadata.create_all(engine)

session = Session()

service = service.Service(session)

# 새로 가입한 사용자
for i in range(100):
    service.account_register()
session.commit()

# 알림
accountIds = service.query_all_accounts().map(lambda x: x.id)
for accountId in accountIds.values.tolist():
    randomizer.random_call(
        service.send_alarm,
        args=[accountId],
        probability=0.1
    )
session.commit()

# 가족 계정 생성
for i in range(5):
    sole_account_ids = service.query_sole_accounts().map(lambda x: x.id)
    family = randomizer.sample(sole_account_ids.values.tolist(), 4)
    service.family_account_register(family)
session.commit()

# 매장 생성
for i in range(10):
    service.store_register()
session.commit()

# 매장 찜
account_ids = service.query_all_accounts().map(lambda x: x.id)
store_ids = service.query_all_stores().map(lambda x: x.id)
for account_id in account_ids.values.tolist():
    for store_id in store_ids.values.tolist():
        randomizer.random_call(
            service.add_favorite,
            args=[account_id, store_id],
            probability=0.01
        )
session.commit()

# 음식 생성
storeIds = service.query_all_stores().map(lambda x: x.id)
for storeId in storeIds.values.tolist():
    for i in range(10):
        service.add_product(storeId)
session.commit()

# 장바구니 담기
accountIds = service.query_all_accounts().map(lambda x: x.id)
storeIds = service.query_all_stores().map(lambda x: x.id)
for accountId in accountIds.values.tolist():
    service.clear_cart(accountId)
    storeId = randomizer.choose(storeIds.values.tolist())
    productIds = service.query_products(storeId).map(lambda x: x.id)
    for productId in productIds.values.tolist():
        randomizer.random_call(
            service.add_cart,
            args=[accountId, productId],
            probability=0.1
        )
session.commit()

# 주문 생성
accountIds = service.query_in_cart_accounts().map(lambda x: x.id)
for accountId in accountIds.values.tolist():
    storeId = service.query_in_cart_store(accountId)
# TODO


session.commit()
