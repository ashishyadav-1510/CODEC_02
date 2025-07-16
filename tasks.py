from celery_app import app
from web_scraper import scrape_news
from database import create_table, insert_data

@app.task
def scheduled_scrape():
    create_table()
    data = scrape_news()
    insert_data(data)
    print(f"Scraped {len(data)} items.")
