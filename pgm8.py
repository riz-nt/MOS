import time
import random
BUFFER_SIZE = 5
buffer = []
buffer_lock = False
buffer_full = 0
def producer_consumer():
    global buffer, buffer_lock, buffer_full
    while True:
        item = random.randint(1, 100)
        if buffer_full == BUFFER_SIZE:
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
# Start the producer-consumer loop
producer_consumer()

