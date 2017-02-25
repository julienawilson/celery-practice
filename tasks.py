from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')
app.conf.CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'


@app.task
def add(x, y):
    return x + y