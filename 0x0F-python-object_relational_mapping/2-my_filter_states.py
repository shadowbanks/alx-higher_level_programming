#!/usr/bin/python3
"""
Module Doc
"""
import sys
import MySQLdb


def main():
    userName, userPwd, dbname, val = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost", user=userName, passwd=userPwd, db=dbname, port=3306
    )
    cur = db.cursor()
    cmd = "SELECT * FROM states WHERE BINARY \
            name LIKE '{}' ORDER BY id".format(val)
    cur.execute(cmd)

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
