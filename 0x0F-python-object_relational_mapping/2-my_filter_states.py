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
    cur.execute(f"SELECT * FROM states WHERE name=%s ORDER BY id", (val,))

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
