###
# reverseTask.py : Executing reverse string task using Celery
###

from celery import Celery

app = Celery(
    'reverseTask',
    broker='amqp://guest@localhost//'
)

@app.task
def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = (s == reversed_s)
    return {
        "original": s,
        "reversed": reversed_s,
        "palindrome": is_palindrome
    }
