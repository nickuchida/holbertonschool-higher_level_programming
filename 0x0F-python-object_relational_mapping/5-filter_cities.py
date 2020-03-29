#!/usr/bin/python3
'''
a script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
'''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM cities, states WHERE \
    state_id=states.id AND states.name = %s ORDER by cities.id', (argv[4],))

    result = cur.fetchall()

    for i in result:
        print(i)
    cur.close()
    db.close()
