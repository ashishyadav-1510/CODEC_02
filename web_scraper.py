from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_news():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.bbc.com/news")  # Example target site

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    articles = soup.find_all('h3')
    news = [(i.text.strip(),) for i in articles if i.text.strip()]
    return news
