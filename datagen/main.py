import json

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from application import services
from application import randomizer

from domain.models import Account, Address, Store

# create an engine to connect to a database
with open('conf.json') as f:
    config = json.load(f)
engine = create_engine(config['db_url'])

# create a session factory
Session = sessionmaker(bind=engine)

# create a base class for our model classes
Base = declarative_base()
Base.metadata.create_all(engine)

session = Session()

# 새로 가입한 사용자
for i in range(100):
    services.account_register(session)

# 알림
account_ids = list(map(lambda x: x[0], session.execute(select(Account.id)).all()))
for account_id in account_ids:
    randomizer.random_call(
        services.send_alarm,
        args=[session, account_id],
        probability=0.1
    )

# 가족 계정 생성
for i in range(5):
    sole_account_ids = list(map(lambda x: x[0], session.execute(
        select(Account.id).where(Account.family_account_id == None)
    ).all()))
    family = randomizer.sample(sole_account_ids, 4)
    services.family_account_register(session, family)

# 매장 생성
for i in range(10):
    services.store_register(session)

# 매장 찜
account_ids = list(map(lambda x: x[0], session.execute(select(Account.id)).all()))
store_ids = list(map(lambda x: x[0], session.execute(select(Store.id)).all()))
for account_id in account_ids:
    for store_id in store_ids:
        randomizer.random_call(
            services.add_favorites,
            args=[session, account_id, store_id],
            probability=0.01
        )

session.commit()
