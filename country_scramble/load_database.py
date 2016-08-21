# Loads the database with country names


import sqlite3

conn = sqlite3.connect('countries.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS countries')
cur.execute('CREATE TABLE countries (country_name TEXT)')

countries = []
with open('countries.txt', 'rb') as country_list:
    for item in country_list:
        countries.append(item)

for item in countries:
    cur.execute("INSERT INTO countries VALUES (?);", [item])

conn.commit()
conn.close()

