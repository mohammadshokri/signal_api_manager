import cx_Oracle
from pathlib import Path
import os
from kucoin.client import Client
# connection for core

def oraConnect():
    os.environ["PATH"] = r"D:\instantclient_21_7;" + os.environ["PATH"]
    os.environ["ORACLE_HOME"] = r"D:\instantclient_21_7"

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    conn = cx_Oracle.connect(user=r'trd_dt', password='trd_dt123', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    return conn
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def setSignal():
    conn = oraConnect()
    with conn.cursor() as cursor:
        # cursor.callproc('PRC_UPD_MARKET', [price, sym])
        # conn.commit()
        try:
            cursor.execute(
                f"select *  from trd_dt.sig_order where status = 1"
            )
            signalList = dictfetchall(cursor)
            print(signalList)
            for s in signalList:

                client = Client(s['API_KEY'], s['API_SECRET'], s['API_PASSPHRASE'] )
                client.create_market_order((s[SYMB], client_oid='client_1'+s['ID'], side= Client.SIDE_BUY, price=s['PR_SYM_DB'], size=100)
                order = client.create_market_order('SLP-USDT', Client.SIDE_BUY,  size=100)
                cursor.callproc('PRC_UPD_SIG', [s['ID'], 2])
        except:
            print("error ")
            cursor.callproc('PRC_UPD_SIG', [s['ID'], 4])



