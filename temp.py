import cx_Oracle

connStr = 'system/9878@localhost:1521/xepdb1'

conn = cx_Oracle.connect(connStr)

    # get a cursor object from the connection
cur = conn.cursor()

cur.close()

        # close the connection object also
conn.close()