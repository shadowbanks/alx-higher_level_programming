#!/usr/bin/python3
"""
Module Doc
"""
import sys
import MySQLdb


def main():
    userName, userPwd, dbname, arg = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost", user=userName, passwd=userPwd, db=dbname, port=3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT c.name"
        + " FROM cities c INNER JOIN states s"
        + " ON c.state_id = s.id"
        + " WHERE %s = s.name"
        " ORDER BY c.id",
        (arg,),
    )

    rows = cur.fetchall()
    print(rows)
    output = ", ".join(row[0] for row in rows)
    print(output)


if __name__ == "__main__":
    main()
