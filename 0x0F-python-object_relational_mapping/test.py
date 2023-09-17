#!/usr/bin/python3
"""
Module Doc
"""
import MySQLdb

db = MySQLdb.connect(
    host="localhost", user="Williams", passwd="Shadowbanks@12", db="test"
)
cur = db.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS song (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL)")
# songs = ("2002", "Ghost", "Somebody To You", "Say You Won't Leg Go")
# for song in songs:
#    cur.execute("INSERT INTO song (title) VALUES (%s)", (song,))
#    print(f"Auto Increment ID: {cur.lastrowid}")

"""
output = cur.execute("SELECT * FROM song WHERE id = %s or id = %s", (1, 2))
print(f"Number of row selected {output}")
print(f"Number of row selected {cur.rowcount}")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print(f"{col}",end="")
    print()
cur.execute("SELECT * FROM song WHERE id = 1")
row = cur.fetchone()
print(f"ID: {row[0]} -- Title: {row[1]}")
"""
try:
    cur.execute("DELETE FROM song WHERE id BETWEEN 5 and 8)")
    # rows = cur.fetchall()
except MySQLdb.Error as e:
    try:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
    except IndexError:
        print(f"MySQL Error: {str(e)}")

try:
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
except MySQLdb.Error as e:
    try:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
    except IndexError:
        print(f"MySQL Error: {str(e)}")
for row in rows:
    for col in row:
        print(f"{col}")
    print()
db.commit()
cur.close()
db.close()
