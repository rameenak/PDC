import threading
import time
import random

class MyThreadClass(threading.Thread):
    def __init__(self, name, animal, lock):
        super().__init__(name=name)
        self.animal = animal
        self.lock = lock

    def run(self):
        # Acquire the lock before printing "running"
        with self.lock:
            print(f"{self.name} {self.animal} is running...", flush=True)

        # Simulate random running time
        run_time = random.uniform(1, 5)
        time.sleep(run_time)

        # Acquire the lock again before printing "finished"
        with self.lock:
            print(f"\n{self.name} {self.animal} finished at {run_time:.2f} seconds!", flush=True)

def main():
    start_time = time.time()
    lock = threading.Lock()

    threads = [
        MyThreadClass("Thread#1", "Cow", lock),
        MyThreadClass("Thread#2", "Tiger", lock),
        MyThreadClass("Thread#3", "Rabbit", lock),
        MyThreadClass("Thread#4", "Dog", lock),
        MyThreadClass("Thread#5", "Lion", lock),
        MyThreadClass("Thread#6", "Horse", lock),
        MyThreadClass("Thread#7", "Monkey", lock),
        MyThreadClass("Thread#8", "Cheetah", lock),
        MyThreadClass("Thread#9", "Turtle", lock),
    ]

    # Start threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"\nThread with Lock End at ... {time.time() - start_time:.2f} seconds", flush=True)

if __name__ == "__main__":
    main()
