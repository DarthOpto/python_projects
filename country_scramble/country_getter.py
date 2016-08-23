import sqlite3
import random


def get_country():
    """
    Gets the country from the database and scrambles it
    :return: country
    """
    country = ""
    conn = sqlite3.connect('countries.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT * FROM countries ORDER BY RANDOM() LIMIT 1;')
    for row in cur:
        country = row[0]
    conn.close()

    country_scrambled = ''.join(random.sample(country, len(country))).upper()
    return country, country_scrambled

