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
    sql = st.get("select_all_from_accounts")

    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

    print(df)

