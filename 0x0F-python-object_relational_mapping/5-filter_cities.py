#!/usr/bin/python3
"""
Module that takes a name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
MySQL Query module using MySQLdb
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities INNER JOIN states ON cities.state_id=states.id
        WHERE states.name = %(value)s ORDER BY cities.id ASC
        """, {'value': argv[4]})
    query_rows = cur.fetchall()
    print(", ".join([tup[0] for tup in query_rows]))
    cur.close()
    conn.close()
