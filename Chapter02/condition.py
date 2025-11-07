import threading
import time
import random

condition = threading.Condition()
current_turn = 0  # used to control which thread runs

class MyThreadClass(threading.Thread):
    def __init__(self, name, animal, index):
        super().__init__(name=name)
        self.animal = animal
        self.index = index

    def run(self):
        global current_turn
        with condition:
            # Wait until it's this thread's turn
            while self.index != current_turn:
                condition.wait()

            # Critical section
            print(f"{self.name} {self.animal} is running...")
            run_time = random.uniform(1, 5)
            time.sleep(run_time)
            print(f"\n{self.name} {self.animal} finished at {run_time:.2f} seconds!\n")

            # Move to the next thread and notify all
            current_turn += 1
            condition.notify_all()


def main():
    start_time = time.time()

    threads = [
        MyThreadClass("Thread#1", "Cow", 0),
        MyThreadClass("Thread#2", "Tiger", 1),
        MyThreadClass("Thread#3", "Rabbit", 2),
        MyThreadClass("Thread#4", "Dog", 3),
        MyThreadClass("Thread#5", "Lion", 4),
        MyThreadClass("Thread#6", "Horse", 5),
        MyThreadClass("Thread#7", "Monkey", 6),
        MyThreadClass("Thread#8", "Cheetah", 7),
        MyThreadClass("Thread#9", "Turtle", 8),
    ]

    for t in threads:
        t.start()

    # Start the first thread
    with condition:
        condition.notify_all()

    for t in threads:
        t.join()

    print(f"Condition with thread end at ... {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
