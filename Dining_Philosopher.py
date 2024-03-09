import threading
import time
import random

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
        self.philosophers = [threading.Thread(target=self.dine, args=(i,)) for i in range(5)]
        for philosopher in self.philosophers:
            philosopher.start()

    def get_forks(self, philosopher_id):
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % 5
        if philosopher_id % 2 == 0:
            self.forks[left_fork].acquire()
            self.forks[right_fork].acquire()
        else:
            self.forks[right_fork].acquire()
            self.forks[left_fork].acquire()

    def release_forks(self, philosopher_id):
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % 5
        self.forks[left_fork].release()
        self.forks[right_fork].release()

    def dine(self, philosopher_id):
        while True:
            self.get_forks(philosopher_id)
            print(f"Philosopher {philosopher_id} is eating.")
            time.sleep(random.uniform(1, 3))
            self.release_forks(philosopher_id)
            print(f"Philosopher {philosopher_id} is thinking.")
            time.sleep(random.uniform(1, 3))

dining_philosophers = DiningPhilosophers()
