###
# addTask.py : RUN the Reverse String Celery Task
###

import reverseTask

if __name__ == '__main__':
    result = reverseTask.reverse_and_check_palindrome.delay("racecar")
    print("Task sent to worker...")
    print("Result:", result.get())
