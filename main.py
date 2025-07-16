import csv
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def configure_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')  # Run in background
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)

def scrape_headlines(driver, url):
    print("Starting manual web scraping process")
    driver.get(url)
    time.sleep(2)  # Allow page to load

    headlines = []
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'titleline')
        headlines = [el.text.strip() for el in elements if el.text.strip()]
        print(f"Scraped {len(headlines)} headlines.")
    except Exception as e:
        print(f"Error while scraping: {e}")
    return headlines

def save_to_database(headlines, db_path='news_data.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS headlines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )''')

    cursor.executemany("INSERT INTO headlines (title) VALUES (?)", [(hl,) for hl in headlines])
    conn.commit()
    conn.close()
    print("Data inserted into SQLite database.")

def export_to_csv(headlines, filename='scraped_news.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])
        writer.writerows([[hl] for hl in headlines])
    print(f"Data exported to {filename}")

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
