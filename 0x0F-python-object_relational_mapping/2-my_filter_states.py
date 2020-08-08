#!/usr/bin/python3
"""
Module that filters states by user input
MySQL Query module using MySQLdb
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    query = """
    SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC
    """.format(argv[4])

    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
