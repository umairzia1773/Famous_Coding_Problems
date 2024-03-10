import threading
import time
import random
from queue import Queue

class ProducerConsumer:
    def __init__(self):
        self.buffer = Queue(maxsize=5)  # Shared buffer with a maximum size of 5
        self.producers = [threading.Thread(target=self.produce) for _ in range(2)]
        self.consumers = [threading.Thread(target=self.consume) for _ in range(2)]

    def produce(self):
        while True:
            item = random.randint(1, 100)
            self.buffer.put(item)
            print(f"Produced {item}. Buffer: {list(self.buffer.queue)}")
            time.sleep(random.uniform(0.5, 1))

    def consume(self):
        while True:
            item = self.buffer.get()
            print(f"Consumed {item}. Buffer: {list(self.buffer.queue)}")
            time.sleep(random.uniform(0.5, 1))

    def start(self):
        for producer in self.producers:
            producer.start()
        for consumer in self.consumers:
            consumer.start()

producer_consumer = ProducerConsumer()
producer_consumer.start()
