#!/usr/bin/python3
""" lists al states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__name__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
               LIKE BINARY 'N%' ORDER BY states.id""")
    row = cur.fetchall()
    for row in row:
        print(row)
    cur.close()
    db.close()
