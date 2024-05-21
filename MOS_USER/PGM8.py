import time
import random


def producer_consumer(buffer_size):
    buffer = []
    buffer_lock = False
    buffer_full = 0

    while True:
        item = random.randint(1, 100)
        if buffer_full == buffer_size:
            print("Buffer is full. Waiting...")
            time.sleep(0.1)  # Wait if buffer is full
        else:
            if buffer_lock:
                print("Buffer is being modified. Waiting...")
                time.sleep(0.1)  # Wait if buffer is being modified
            else:
                buffer_lock = True  # Acquire the lock
                buffer.append(item)  # Add item to the buffer
                buffer_full += 1
                print(f"Produced {item}, Buffer: {buffer}")
                buffer_lock = False  # Release the lock

                if random.random() < 0.5:
                    if buffer_full == 0:
                        print("Buffer is empty. Waiting...")
                        time.sleep(0.1)  # Wait if buffer is empty
                    else:
                        if buffer_lock:
                            print("Buffer is being modified. Waiting...")
                            time.sleep(0.1)  # Wait if buffer is being modified
                        else:
                            buffer_lock = True  # Acquire the lock
                            item = buffer.pop(0)  # Remove item from the buffer
                            buffer_full -= 1
                            print(f"Consumed {item}, Buffer: {buffer}")
                            buffer_lock = False  # Release the lock
        time.sleep(random.uniform(0.1, 1))


if __name__ == "__main__":
    buffer_size = int(input("Enter the buffer size: "))
    producer_consumer(buffer_size)
