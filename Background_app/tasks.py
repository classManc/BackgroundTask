from celery import shared_task

@shared_task()
def greet():
    # function that returns "Hello word"
    # decorated by @shared_task so that it can become a celery task
    return 'Hello World'

