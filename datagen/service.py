import json
import pymysql

from common.statements import Statements


def orders():
    with open('conf.json') as f:
        config = json.load(f)
    db = pymysql.connect(**config)

    cursor = db.cursor()

    st = Statements('mysql-statements.xml')
    sql = st.get("select_all_from_orders")

    df = cursor.execute(sql)


