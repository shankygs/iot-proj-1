from flask import Flask, redirect, url_for, request, render_template
import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor


from models import *

app = Flask(__name__)
#from config import config

@app.route('/get/enterprise', methods=["GET"] )
def get_enterprise():
    conn="None"
    connection_parameters = {
        'host': 'localhost',
        'database': 'SHANKY',
        'user': 'SHANKY',
        'password': 'root123',
        'port': '5432'
    }

    try:
        #params = config()

        print ("Connecting to postgresql")
        conn=psycopg2.connect(**connection_parameters)

        cur = conn.cursor(cursor_factory=RealDictCursor)

        print("Postgres SQL database Version")
        cur.execute('SELECT version()')
        db_version=cur.fetchone()
        print(db_version)

        cur.execute("SELECT * from enterprises;")
        #rows=cur.fetchall()
        entlist = json.dumps(cur.fetchall(), indent=2)
        print(entlist)
        #return(json.dumps(cur.fetchall(), indent=2))
        #return flask.jsonify(rows)
        #for row in rows:
        #    print(row)
        cur.close()
        return entlist
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        print('Database connection closed.')

if __name__ == '__main__':
    app.run()
