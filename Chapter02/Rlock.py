import threading
import time
import random

class MyThreadClass(threading.Thread):
    def __init__(self, name, animal, rlock):
        super().__init__(name=name)
        self.animal = animal
        self.rlock = rlock

    def run(self):
        # Acquire RLock before printing
        with self.rlock:
            print(f"{self.name} {self.animal} is running...")

        run_time = random.uniform(1, 5)
        time.sleep(run_time)

        # Call a nested function that also uses the same RLock
        self.nested_print(run_time)

    def nested_print(self, run_time):
        # Same thread can re-acquire the same lock (safe with RLock)
        with self.rlock:
            print(f"\n{self.name} {self.animal} finished at {run_time:.2f} seconds!")


def main():
    start_time = time.time()
    rlock = threading.RLock()  # Create reentrant lock

    threads = [
        MyThreadClass("Thread#1", "Cow", rlock),
        MyThreadClass("Thread#2", "Tiger", rlock),
        MyThreadClass("Thread#3", "Rabbit", rlock),
        MyThreadClass("Thread#4", "Dog", rlock),
        MyThreadClass("Thread#5", "Lion", rlock),
        MyThreadClass("Thread#6", "Horse", rlock),
        MyThreadClass("Thread#7", "Monkey", rlock),
        MyThreadClass("Thread#8", "Cheetah", rlock),
        MyThreadClass("Thread#9", "Turtle", rlock),
    ]

    # Start threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"\nRlock thread ends at ... {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
