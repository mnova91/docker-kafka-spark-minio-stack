from confluent_kafka import Producer

# Kafka config
conf = {'bootstrap.servers': 'localhost:9092'}
p = Producer(conf)

def delivery_callback(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}")

# Produce a single test message
p.produce('test-topic', 'hello from Python', callback=delivery_callback)
p.flush(10)
