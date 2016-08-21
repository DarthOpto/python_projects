import sqlite3


class CountryGetter:

    @staticmethod
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
            country = str(row[0].decode("utf-8").rstrip())
        conn.close()
        return country