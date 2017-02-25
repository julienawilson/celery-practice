from celery import Celery
from tasks import add

app = Celery('learncelery', broker='redis://localhost:6379/0')


@app.task
def hello():
    return 'hello world'


def repeat_add(num):
    """Repeat the add function a few times."""
    result = []
    for i in range(num):
        result.append(add.delay(i, i))
    return result
