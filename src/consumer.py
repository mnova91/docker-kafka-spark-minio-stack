from confluent_kafka import Consumer, TopicPartition

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': 'test-group',               # Consumer group id
    'auto.offset.reset': 'earliest'         # Start from the earliest message if no offset is committed
}

# Create a Consumer instance
c = Consumer(conf)

# Explicitly assign to partition 0 of 'test-topic' at offset 0
c.assign([TopicPartition('test-topic', 0, 0)])

# Poll for a message (wait up to 10 seconds)
msg = c.poll(timeout=10.0)
if msg is None:
    print("No message received within timeout")
elif msg.error():
    print(f"Error: {msg.error()}")
else:
    # Print the received message and its offset
    print(f"Received message: {msg.value().decode('utf-8')} at offset {msg.offset()}")

# Close the consumer to commit final offsets and clean up resources
c.close()
