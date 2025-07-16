import sqlite3
import pandas as pd

def export_to_csv():
    conn = sqlite3.connect("news_data.db")
    df = pd.read_sql_query("SELECT * FROM news", conn)
    df.to_csv("scraped_news.csv", index=False)
    print("Exported to scraped_news.csv")
    conn.close()
