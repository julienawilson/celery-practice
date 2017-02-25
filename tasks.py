from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')
# app = Celery('tasks',  broker='amqp://guest@localhost//')

app.conf.result_backend = 'redis://'


@app.task
def add(x, y):
    return x + y


def repeat_add(num):
    """Repeat the add function a few times."""
    result = []
    for i in range(num):
        result.append(add.delay(i, i))
    return result
