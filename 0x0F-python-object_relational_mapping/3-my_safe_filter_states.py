#!/usr/bin/python3
"""
Module that filters states by user input, safe from MySQL injections.
MySQL Query module using MySQLdb
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(value)s ORDER BY id ASC",
                {'value': argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
