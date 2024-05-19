import time
import random
NUM_PHILOSOPHERS = 5
MAX_EATING_TIME = 3
forks = [True] * NUM_PHILOSOPHERS  # True indicates the fork is available
def philosopher(index):
    for _ in range(MAX_EATING_TIME):
        think(index)
        eat(index)
def think(index):
    print(f"Philosopher {index} is thinking...")
    time.sleep(random.uniform(0.1, 1))
def eat(index):
    print(f"Philosopher {index} is hungry and trying to pick up forks...")
    left_fork = index
    right_fork = (index + 1) % NUM_PHILOSOPHERS
    while True:
        if forks[left_fork] and forks[right_fork]:
            forks[left_fork] = False
            forks[right_fork] = False
            print(f"Philosopher {index} is eating...")
            time.sleep(random.uniform(0.1, 1))
            forks[left_fork] = True
            forks[right_fork] = True
            break
        else:
            print(f"Philosopher {index} couldn't acquire forks. Retrying...")
            time.sleep(0.1)
if __name__ == "__main__":
    for i in range(NUM_PHILOSOPHERS):
        philosopher(i)
    print("Dinner is over. Philosophers are full and content.")
