import uuid

from domain.models import Account, FamilyAccount, Address, Alarm
from application import randomizer
from sqlalchemy.testing.pickleable import Order

from datagen.domain.models import Store, Favorite


def random_account() -> Account:
    return Account(
        id=uuid.uuid4().hex,
        email=randomizer.email(),
        password=uuid.uuid4(),
        nickname=randomizer.name_korean(randomizer.random_binary(0.5)),
        phone_number="010-" + randomizer.numbers(4) + "-" + randomizer.numbers(4),
        virtual_number="05" + randomizer.numbers(2) + "-" + randomizer.numbers(4) + "-" + randomizer.numbers(4),
        payment=randomizer.choose(["카카오페이", "네이버페이", "신용카드"]),
        family_account_id=None,
        points=0,
        rank="일반",
        role="USER"
    )

def random_family_account(owner_id) -> FamilyAccount:
    return FamilyAccount(
        id=uuid.uuid4().hex,
        account_id=owner_id,
        payment=randomizer.choose(["카카오페이", "네이버페이", "신용카드"]),
        orders_left=randomizer.choose([10, 20, 30])
    )

def random_address(user_id) -> Address:
    return Address(
        id=uuid.uuid4().hex,
        account_id=user_id,
        name="기본주소",
        first_address="서울시",
        second_address="99호",
        favor=randomizer.choose(["조심히 배달해주세요", "문 앞에 놓아주세요", "부재 시 연락 주세요"])
    )


def random_alarm(user_id) -> Alarm:
    return Alarm(
        id=uuid.uuid4().hex,
        account_id=user_id,
        title="알림 제목",
        content="알림 내용",
        link="알림 링크",
    )

def random_store() -> Store:
    return Store(
        id=uuid.uuid4().hex,
        status="영업중",
        name="일반음식점",
        address="서울시 어딘가",
        business_hours="오후 1시 ~ 오후 9시",
        day_off="4/1,4/15",
        description="안녕하세요 맛있는 식당 입니다",
        min_orders=15000,
        phone_number="010-" + randomizer.numbers(4) + "-" + randomizer.numbers(4),
        owner=randomizer.name_korean(randomizer.random_binary(0.5)),
        taxpayer_address="서울시 어딘가",
        taxpayer_id_number="00-000-00000",
        ingredients="돼지고기(국산),김치(중국산)"
    )

def favorite(account_id, store_id) -> Favorite:
    return Favorite(
        id=uuid.uuid4().hex,
        account_id=account_id,
        store_id=store_id
    )