from confluent_kafka import Producer

# Kafka config
conf = {'bootstrap.servers': 'localhost:9092'}  # Kafka broker address
p = Producer(conf)

def delivery_callback(err, msg):
    """
    Callback function to report message delivery result.
    """
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

# Produce a single test message to 'test-topic'
p.produce('test-topic', 'hello from Python', callback=delivery_callback)

# Wait for any outstanding messages to be delivered (timeout: 10 seconds)
p.flush(10)
