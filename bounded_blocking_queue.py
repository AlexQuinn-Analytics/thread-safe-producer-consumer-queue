import threading
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity):
        """
        Initialize the queue with a fixed capacity.
        Use a deque for queue storage.
        Initialize a lock and two condition variables to manage synchronization.
        """
        self.queue = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)  # For waiting when queue is empty
        self.not_full = threading.Condition(self.lock)   # For waiting when queue is full

    def put(self, item):
        """
        Add an item to the queue.
        If the queue is full, wait until a slot is free.
        """
        with self.not_full:
            while len(self.queue) >= self.capacity:
                self.not_full.wait()  # Wait for space to become available
            self.queue.append(item)
            self.not_empty.notify()  # Notify consumers that queue is not empty

    def get(self):
        """
        Remove and return an item from the queue.
        If the queue is empty, wait until an item is available.
        """
        with self.not_empty:
            while not self.queue:
                self.not_empty.wait()  # Wait for items to be available
            item = self.queue.popleft()
            self.not_full.notify()  # Notify producers that queue has space
            return item

    def size(self):
        """
        Return the current size of the queue in a thread-safe manner.
        """
        with self.lock:
            return len(self.queue)


# Example usage with multiple producers and consumers

import time
import random

def producer(q, id, items_to_produce):
    for item in items_to_produce:
        q.put(item)
        print(f"Producer {id} produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(q, id, consume_count):
    for _ in range(consume_count):
        item = q.get()
        print(f"Consumer {id} consumed: {item}")
        time.sleep(random.uniform(0.1, 0.5))


if __name__ == "__main__":
    queue_capacity = 5
    q = BoundedBlockingQueue(queue_capacity)

    producer_threads = [
        threading.Thread(target=producer, args=(q, 1, range(10))),
        threading.Thread(target=producer, args=(q, 2, range(10, 20)))
    ]

    consumer_threads = [
        threading.Thread(target=consumer, args=(q, 1, 10)),
        threading.Thread(target=consumer, args=(q, 2, 10))
    ]

    for t in producer_threads + consumer_threads:
        t.start()

    for t in producer_threads + consumer_threads:
        t.join()

    print("All producers and consumers have finished.")
