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
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101900.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101910.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101926.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20104539.png?raw=true)

### Output:
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101900.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101910.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101926.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20104539.png?raw=true)

#### CSV FILE
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101900.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101910.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101926.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20104539.png?raw=true)

#### DB FILE
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101900.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101910.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20101926.png?raw=true)
![image](https://github.com/ashishyadav-1510/CODEC_01/blob/main/Screenshot/Screenshot%202025-07-16%20104539.png?raw=true)

### Author
***Ashish Yadav***