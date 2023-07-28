import requests
from bs4 import BeautifulSoup
import sqlite3

# specify the URL of the website you want to scrape
url = "https://www.example.com"

# send an HTTP request to the website and retrieve the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# extract the desired data from the HTML content using BeautifulSoup
data = []
for element in soup.find_all("div", class_="example-class"):
    data.append(element.get_text())

# set up a connection to a local SQLite database
conn = sqlite3.connect("example.db")

# create a table in the database to store the scraped data
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS example_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL
    );
    """
)

# parse the scraped data and insert it into the local database table
for item in data:
    cursor.execute(
        """
        INSERT INTO example_data (data)
        VALUES (?);
        """, (item,)
    )
conn.commit()

# close the database connection
conn.close()
