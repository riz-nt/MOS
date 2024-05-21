import time
import random

def philosopher(index, max_eating_time):
    for _ in range(max_eating_time):
        think(index)
        eat(index)

def think(index):
    print(f"Philosopher {index} is thinking...")
    time.sleep(random.uniform(0.1, 1))

def eat(index):
    global forks
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
    NUM_PHILOSOPHERS = int(input("Enter the number of philosophers: "))
    MAX_EATING_TIME = int(input("Enter the maximum eating time: "))

    forks = [True] * NUM_PHILOSOPHERS  # True indicates the fork is available

    for i in range(NUM_PHILOSOPHERS):
        philosopher(i, MAX_EATING_TIME)

    print("Dinner is over. Philosophers are full and content.")
