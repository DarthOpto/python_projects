import requests
import selectorlib
from smtplib import SMTP_SSL as SMTP
import os
import time
import sqlite3

"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT * FROM events WHERE date='2088.10.15'"

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}




class Tour:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "curtis.salisbury@gmail.com"
        password = "lgovidjtlsdisajc"
        receiver = "curtis.salisbury@gmail.com"

        with SMTP(host, port):
            server = SMTP(host)
            server.login(username, password)
            server.sendmail(username, receiver, message)


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)

    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows


if __name__ == "__main__":
    while True:
        tour = Tour()
        scraped = tour.scrape(URL)
        extracted = tour.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            data = Database(database_path="data.db")
            row = data.read(extracted)
            if not row:
                data.store(extracted)
                email = Email()
                email.send(message="Hey, new event was found!")
        time.sleep(2)
