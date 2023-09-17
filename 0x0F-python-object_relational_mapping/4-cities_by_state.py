#!/usr/bin/env python3
import sys
import MySQLdb


def main():
    userName, userPwd, dbname = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost", user=userName, passwd=userPwd, db=dbname, port=3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT c.id, c.name, s.name"
        + " FROM cities c INNER JOIN states s"
        + " ON c.state_id = s.id"
        + " ORDER BY id"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
