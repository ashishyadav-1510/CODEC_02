# 📰 Automated News Web Scraper
This project is a **Python-based web scraping pipeline** that automatically scrapes news headlines from websites like [Hacker News](https://news.ycombinator.com) and [BBC News](https://www.bbc.com/news), stores them in an SQLite database, and exports them to a CSV file. It uses **Selenium**, **BeautifulSoup**, **Celery**, and **SQLite**, with scheduled scraping every 2 minutes via **Celery Beat**.

## 🚀 Features

- ✅ Scrapes headlines using **Selenium** and **BeautifulSoup**
- ✅ Stores data in a **SQLite** database
- ✅ Exports scraped data to **CSV**
- ✅ **Automated scheduling** using **Celery + Redis + Celery Beat**
- ✅ Logs number of headlines scraped

## 🧱 Tech Stack

| Tool          | Purpose                         |
|---------------|----------------------------------|
| Python        | Core programming language        |
| Selenium      | Dynamic content scraping         |
| BeautifulSoup | HTML parsing                     |
| SQLite3       | Lightweight database             |
| Pandas        | Exporting to CSV                 |
| Celery        | Task queue for scheduling tasks  |
| Redis         | Celery message broker            |


## 🗂️ Project Structure
Codec2/
│
├── web_scraper.py # Scrapes headlines from websites
├── database.py # SQLite database functions
├── celery_app.py # Celery configuration
├── tasks.py # Celery task definition
├── beat_schedule.py # Celery Beat periodic schedule
├── export_csv.py # Exports headlines from DB to CSV
├── main_scraper.py # Manual scraping and saving
├── scraped_news.csv # Output CSV (auto-generated)
├── news_data.db # SQLite DB file (auto-generated)
└── README.md # Project documentation

## 🔧 Installation & Setup
1. **Clone the repository**

git clone https://github.com/your-username/news_scraper.git
cd news_scraper
Install dependencies

pip install -r requirements.txt
Example requirements.txt:

selenium
beautifulsoup4
pandas
celery
redis
Start Redis server

redis-server
Run Celery worker and Beat scheduler in separate terminals

celery -A tasks worker --loglevel=info
celery -A beat_schedule beat --loglevel=info
Run manual scraper (optional)
python main_scraper.py
## 🔁 Scheduled Scraping
The scraping runs every 2 minutes automatically. You can modify the interval in beat_schedule.py:
'schedule': crontab(minute='*/2'),  # Change as needed
## 🛠️ How It Works
main_scraper.py: Manually scrapes from Hacker News and stores in DB/CSV.
web_scraper.py: Uses Selenium + BeautifulSoup to scrape BBC headlines.
database.py: Handles DB creation and insertion.
tasks.py: Defines the scheduled Celery task.
celery_app.py: Celery app configuration.
beat_schedule.py: Schedules tasks every 2 minutes.

## 📦 Output
SQLite DB: news_data.db with timestamped headlines
CSV: scraped_news.csv containing all saved headlines

## 📸 Sample Output (CSV)
id	headline	scraped_at
1	NASA to Launch Europa Clipper	2025-07-16 10:02:00
2	AI Revolution in Healthcare	2025-07-16 10:04:00

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115539.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115551.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115604.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115614.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115621.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115637.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115650.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115701.png?raw=true)

### Output:
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115730.png?raw=true)
#### CSV FILE
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115827.png?raw=true)
#### DB FILE
![image](https://github.com/ashishyadav-1510/CODEC_02/blob/main/Screenshot/Screenshot%202025-07-16%20115757.png?raw=true)

## Video
[Video on YouTube]()

## Explaination
🔹 main.py — Manual Scraping with Selenium

import csv
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

Import necessary libraries:
csv for file writing.
sqlite3 for database.
time to pause and let pages load.
selenium libraries to automate browser actions.

Function: configure_driver()
def configure_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')  # Run in background
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)
Sets ChromeDriver options for headless scraping (no GUI).
Ignores SSL/Certificate errors.
Returns a webdriver.Chrome instance configured for headless use.

Function: scrape_headlines(driver, url)
def scrape_headlines(driver, url):
    print("Starting manual web scraping process")
    driver.get(url)
    time.sleep(2)  # Allow page to load
Loads the target URL.
Waits 2 seconds to let JavaScript render fully.

    headlines = []
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'titleline')
        headlines = [el.text.strip() for el in elements if el.text.strip()]
        print(f"Scraped {len(headlines)} headlines.")
Scrapes all elements with class titleline (used in Hacker News).
Extracts non-empty headline texts.

    except Exception as e:
        print(f"Error while scraping: {e}")
    return headlines
Catches and prints any scraping error.

Function: save_to_database()
def save_to_database(headlines, db_path='news_data.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS headlines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )''')
Connects to SQLite DB.
Creates headlines table if it doesn’t exist.

    cursor.executemany("INSERT INTO headlines (title) VALUES (?)", [(hl,) for hl in headlines])
    conn.commit()
    conn.close()
    print("Data inserted into SQLite database.")
Inserts each headline.
Commits and closes the DB connection.

Function: export_to_csv()
def export_to_csv(headlines, filename='scraped_news.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])
        writer.writerows([[hl] for hl in headlines])
    print(f"Data exported to {filename}")
Opens a CSV file.
Writes column header and then each headline in a row.
Main Execution Block

if __name__ == '__main__':
    URL = 'https://news.ycombinator.com/'

    driver = configure_driver()
    headlines = scrape_headlines(driver, URL)
    driver.quit()

    if headlines:
        save_to_database(headlines)
        export_to_csv(headlines)
    else:
        print("No headlines found. Nothing saved.")
Runs scraping, then saves to database and CSV if headlines were found.

🔹 tasks.py — Celery Task File

from celery_app import app
from web_scraper import scrape_news
from database import create_table, insert_data

@app.task
def scheduled_scrape():
    create_table()
    data = scrape_news()
    insert_data(data)
    print(f"Scraped {len(data)} items.")
Defines a Celery task (scheduled_scrape) that:
Creates the DB table (if not exists),
Calls the scraping function,
Inserts data,
Logs how many headlines were scraped.

🔹 web_scraper.py — BeautifulSoup Scraper

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
Imports Selenium and BeautifulSoup for HTML parsing.

def scrape_news():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.bbc.com/news")  # Example target site
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
Opens BBC News in a headless browser.
Parses HTML with BeautifulSoup.

    articles = soup.find_all('h3')
    news = [(i.text.strip(),) for i in articles if i.text.strip()]
    return news
Extracts all <h3> tag texts (commonly used for headlines).
Returns list of tuples (format required for DB insertion).

🔹 database.py — SQLite Helpers

import sqlite3
def connect():
    return sqlite3.connect("news_data.db")
Connects to SQLite DB.

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
Creates news table with automatic timestamp.

def insert_data(news_list):
    conn = connect()
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO news (headline) VALUES (?)', news_list)
    conn.commit()
    conn.close()
Inserts all headlines into the DB.

🔹 export.py — Export SQLite to CSV
import sqlite3
import pandas as pd

def export_to_csv():
    conn = sqlite3.connect("news_data.db")
    df = pd.read_sql_query("SELECT * FROM news", conn)
    df.to_csv("scraped_news.csv", index=False)
    print("Exported to scraped_news.csv")
    conn.close()
Reads DB into Pandas DataFrame.
Exports entire table to scraped_news.csv.

🔹 celery_app.py — Celery App Configuration
from celery import Celery

app = Celery('scraper', broker='redis://localhost:6379/0', backend='rpc://')
Sets up Celery app with Redis as broker (for task queue) and RPC as result backend.

🔹 beat_scheduler.py — Celery Beat Task Schedule
from celery.schedules import crontab
from celery_app import app
from tasks import scheduled_scrape

app.conf.beat_schedule = {
    'scrape-every-2-minutes': {
        'task': 'tasks.scheduled_scrape',
        'schedule': crontab(minute='*/2'),  # every 2 minutes
    },
}
app.conf.timezone = 'Asia/Kolkata'
Configures periodic task using celery-beat.
Executes scheduled_scrape() every 2 minutes.
Sets timezone to IST (Asia/Kolkata).

### Author
***Ashish Yadav***