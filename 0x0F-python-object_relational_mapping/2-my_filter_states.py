#!/usr/bin/env python3
import sys
import MySQLdb

def main():
    userName, userPwd, dbname, searchVal = sys.argv[1:5]

    db = MySQLdb.connect(host='localhost', user=userName, passwd=userPwd, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name=%s ORDER BY id", (searchVal,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
