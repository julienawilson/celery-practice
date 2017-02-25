from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')
# app = Celery('tasks',  broker='amqp://guest@localhost//')

app.conf.result_backend = 'redis://'

@app.task
def add(x, y):
    return x + y