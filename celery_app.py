from celery import Celery

app = Celery('scraper', broker='redis://localhost:6379/0', backend='rpc://')
