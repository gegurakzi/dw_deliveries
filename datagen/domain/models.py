from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    nickname = Column(String)
    phone_number = Column(String)
    virtual_number = Column(String)
    payment = Column(String)
    family_account_id = Column(ForeignKey('family_accounts.id'), nullable=True)
    points = Column(Integer)
    rank = Column(String)
    role = Column(Integer)
    created_on = Column(DateTime, default=datetime.utcnow)
    last_updated_on = Column(DateTime, default=datetime.utcnow)


class FamilyAccount(Base):
    __tablename__ = 'family_accounts'

    id = Column(String, primary_key=True)
    account_id = Column(ForeignKey('accounts.id'))
    payment = Column(String)
    orders_left = Column(Integer)
    created_on = Column(DateTime, default=datetime.utcnow)
    last_updated_on = Column(DateTime, default=datetime.utcnow)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(String, primary_key=True)
    account_id = Column(ForeignKey('accounts.id'))
    name = Column(String)
    first_address = Column(String)
    second_address = Column(String)
    favor = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)
    last_updated_on = Column(DateTime, default=datetime.utcnow)


class Alarm(Base):
    __tablename__ = 'alarms'

    id = Column(String, primary_key=True)
    account_id = Column(ForeignKey('accounts.id'))
    title = Column(String)
    content = Column(String)
    link = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)
    last_updated_on = Column(DateTime, default=datetime.utcnow)

class Store(Base):
    __tablename__ = 'stores'

    id = Column(String, primary_key=True)
    status = Column(String)
    name = Column(String)
    address = Column(String)
    business_hours = Column(String)
    day_off = Column(String)
    description = Column(String)
    min_orders = Column(Integer)
    phone_number = Column(String)
    owner = Column(String)
    taxpayer_address = Column(String)
    taxpayer_id_number = Column(String)
    ingredients = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)
    last_updated_on = Column(DateTime, default=datetime.utcnow)


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(String, primary_key=True)
    account_id = Column(ForeignKey('accounts.id'))
    store_id = Column(ForeignKey('stores.id'))
    created_on = Column(DateTime, default=datetime.utcnow)
    last_updated_on = Column(DateTime, default=datetime.utcnow)
