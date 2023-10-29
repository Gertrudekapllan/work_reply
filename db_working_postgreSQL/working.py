from pydoc import text

import psycopg2
from decouple import config
from sqlparse import engine

conn = psycopg2.connect(database="sportsmen",
                        user="postgres",
                        password="3823krasivoe",
                        host="127.0.0.1",
                        port="5432")
print("success connect!!!")

cur = conn.cursor()
cur.execute("select id, sportsman_name from sportsman")
list_sportsmen_test = cur.fetchall()
for i in list_sportsmen_test:
    if i[0] == 1:
        print(i)
print(list_sportsmen_test)

cur.execute("select id, sportsman_name, year_of_birth, country, rank from sportsman")
list_sportsmen_full = cur.fetchall()
count = 0
new_list_result = []
for i in list_sportsmen_full:
    if i[3] == 'Москва':
        print(i)
        new_list_result.append(i)
print(new_list_result)

conn.commit()
conn.close()
