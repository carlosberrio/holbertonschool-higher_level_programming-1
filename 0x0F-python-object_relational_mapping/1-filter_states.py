#!/usr/bin/python3
""" 1-filter_states
Module that lists all states with a name starting with N (upper N)
MySQL Query module using MySQLdb
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC
    """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
