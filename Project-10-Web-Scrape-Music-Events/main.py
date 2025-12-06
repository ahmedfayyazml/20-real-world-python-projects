import  requests
import selectorlib
from  emailing import SendEmail
import  time
import  sqlite3

from example import connection

"INSERT INTO events VALUES('Tigers','Tiger City','2088.10.14')"
"SELECT* FROM events WHERE data = '2088.10.14'"
"DELETE FROM events WHERE name = 'Lions'"


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL  = "https://programmer100.pythonanywhere.com/tours/"

class Event:

    def scrape(self,url):
        """SCRAPE THE PAGE SOURCE FROM URL"""
        response = requests.get(url,headers=HEADERS)
        source = response.text
        return  source

    def extract(self,source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
    def store(self,extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
        self.connection.commit()

    def read(self,extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band,city,date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT* FROM events WHERE band = ? AND city = ? AND date = ?",(band,city,date))
        row = cursor.fetchall()
        return row


if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)  # Optional: helps you see what is being scraped

        # FIX: Check if extracted data is valid BEFORE calling read()
        if extracted != "No upcoming tours":
            database = DataBase()
            send_email = SendEmail()
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                send_email.send_email(extracted)

        time.sleep(2)



