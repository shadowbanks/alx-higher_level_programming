#!/usr/bin/python3
"""
Module Doc
"""


import sys
import MySQLdb


if __name__ == "__main__":
    userName, userPwd, dbName = sys.argv[1:4]
    db = MySQLdb.connect(
        host="localhost", user=userName, passwd=userPwd, db=dbName, port=3306
    )
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
