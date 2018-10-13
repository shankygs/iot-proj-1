import psycopg2
from config import config

def connect():
    conn="None"

    try:
        params = config()

        print ("Connecting to postgresql")
        conn=psycopg2.connect(**params)

        cur = conn.cursor()

        print("Postgres SQL database Version")
        cur.execute('SELECT version()')
        db_version=cur.fetchone()
        print(db_version)

        cur.execute('SELECT * from enterprise')
        rows=cur.fetchall()
        for row in rows:
            print(rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
