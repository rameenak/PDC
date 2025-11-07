import threading
import time
import random

# Semaphore limits how many threads can run concurrently
semaphore = threading.Semaphore(3)  # allow only 3 threads at a time

class MyThreadClass(threading.Thread):
    def __init__(self, name, animal):
        super().__init__(name=name)
        self.animal = animal

    def run(self):
        # Acquire semaphore before entering the critical section
        with semaphore:
            print(f"{self.name} {self.animal} is running...")
            run_time = random.uniform(1, 5)
            time.sleep(run_time)
            print(f"\n{self.name} {self.animal} finished at {run_time:.2f} seconds!")

def main():
    start_time = time.time()

    threads = [
        MyThreadClass("Thread#1", "Cow"),
        MyThreadClass("Thread#2", "Tiger"),
        MyThreadClass("Thread#3", "Rabbit"),
        MyThreadClass("Thread#4", "Dog"),
        MyThreadClass("Thread#5", "Lion"),
        MyThreadClass("Thread#6", "Horse"),
        MyThreadClass("Thread#7", "Monkey"),
        MyThreadClass("Thread#8", "Cheetah"),
        MyThreadClass("Thread#9", "Turtle"),
    ]

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"\nThread with semaphore end at ... {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
