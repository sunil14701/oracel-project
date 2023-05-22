import cx_Oracle

# connection string in the format
# <username>/<password>@<dbHostAddress>:<dbPort>/<dbServiceName>
connStr = 'system/9878@localhost:1521/xepdb1'

# initialize the connection object
conn = None
try:
    # create a connection object
    conn = cx_Oracle.connect(connStr)

    # get a cursor object from the connection
    cur = conn.cursor()

    # prepare data insertion rows
    dataInsertionTuples = [
        ('India', 'Oil', 'uranium'),
        ('Pakistan','goat','boat') 
    ]

    # # create sql for deletion of existing rows to avoid insert conflicts
    # sqlTxt = 'DELETE from "test1".students where\
    #             (st_name=:1 and dob=:2)\
    #             or (studentid=:3)'
    # # execute the sql to perform deletion
    # cur.executemany(sqlTxt, [x for x in dataInsertionTuples])

    # rowCount = cur.rowcount
    # print("number of existing rows deleted =", rowCount)

    # create sql for data insertion
    # sqlTxt = '''insert into "test1".top_product(country, "2010", "2011") values('Pakistan','goat','boat')'''
    sqlTxt = '''insert into "test1".top_product(country, "2010", "2011") values(:1, :2, :3)'''
    # execute the sql to perform data extraction
    # cur.executemany(sqlTxt, dataInsertionTuples)
    cur.execute(sqlTxt,('qgPIndia', 'Oil', 'uranium'))

    # rowCount = cur.rowcount
    # print("number of inserted rows =", rowCount)

    # commit the changes
    conn.commit()
    print("hello")
except Exception as err:
    print('Error while inserting rows into db')
    print(err)
finally:
    if(conn):
        # close the cursor object to avoid memory leaks
        cur.close()

        # close the connection object also
        conn.close()
print("data insert example execution complete!")