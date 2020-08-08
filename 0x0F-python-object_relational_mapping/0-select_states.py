#!/usr/bin/python3
"""
# Module that lists all states from the database hbtn_0e_0_usa
using module MySQLdb (import MySQLdb):
Connects to a MySQL server running on localhost at port 3306
Port 3306 is the default port for the MySQL Protocol ( port ), which is used
by the mysql client, MySQL Connectors, and utilities such as
mysqldump and mysqlpump.
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
