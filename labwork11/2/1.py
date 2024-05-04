import psycopg2
import csv
from tabulate import tabulate 

conn = psycopg2.connect(host="localhost", dbname="book", user="postgres",
                        password="jujutsukaisen", port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists contact (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL
)
""")

def updateing():
    column = input('Which column do you want to change: ')
    value = input(f"Which value do you want to change: ")
    new_value = input(f"New value: ")
    cur.execute(f"UPDATE contact SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

updateing()