from celery import Celery

app = Celery('learncelery', broker='redis://localhost:6379/0')


@app.task
def hello():
    return 'hello world'
