import time
import random

class MyClass:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal

    def run(self):
        print(f"{self.name} {self.animal} is running...")
        run_time = random.uniform(1, 5)
        time.sleep(run_time)
        print(f"{self.name} {self.animal} finished at {run_time:.2f} seconds!")

def main():
    start_time = time.time()

    animals = [
        MyClass("Thread#1", "Cow"),
        MyClass("Thread#2", "Tiger"),
        MyClass("Thread#3", "Rabbit"),
        MyClass("Thread#4", "Dog"),
        MyClass("Thread#5", "Lion"),
        MyClass("Thread#6", "Horse"),
        MyClass("Thread#7", "Monkey"),
        MyClass("Thread#8", "Cheetah"),
        MyClass("Thread#9", "Turtle"),
    ]

    # Run sequentially (no threading)
    for a in animals:
        a.run()

    print(f"\nAll finished in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
