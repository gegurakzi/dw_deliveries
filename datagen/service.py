import json
import pymysql
import pandas as pd

from common.statements import Statements


def orders():
    with open('conf.json') as f:
        config = json.load(f)
    db = pymysql.connect(**config)

    cursor = db.cursor()

    st = Statements('mysql-statements.xml')

    # [ [ 계정, [매장 -> 배달 정보 ] ] -> 주문, 장바구니 ] -> 주문 라인
    # query accounts to order
    cursor.execute(st.get("query_account_to_order"))
    account_df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

    # query stores to order
    cursor.execute(st.get("query_store_to_order"))
    store_df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

    # query delivery info of store to order
    cursor.execute(st.get("query_delivery_info_of_store_to_order"))
    delivery_info_df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

    # query carts of cart to order line
    cursor.execute(st.get("query_carts_of_cart_to_orderline"))
    carts_df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

    # create order with account, store, delivery info, order line
    cursor.execute(st.get("insert_order", param={
        "id": "",
        "accountId": "",
        "storeId": "",
        "status": "",
        ...
    }))

    # create order line with order, product
    cursor.execute(st.get("insert_orderline", param={
        "id": "",
        "orderId": "",
        "productId": "",
        "option": "",
        "amount": "",
        "createdOn": "",
        "lastUpdatedOn": ""
    }))

    cursor.execute(st.get("update_order_placement"))