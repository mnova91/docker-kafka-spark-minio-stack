from confluent_kafka import Consumer, TopicPartition

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest'
}
c = Consumer(conf)

# Explicitly assign partition 0 at offset 0
c.assign([TopicPartition('test-topic', 0, 0)])

msg = c.poll(timeout=10.0)
if msg is None:
    print("No message received within timeout")
elif msg.error():
    print(f"Error: {msg.error()}")
else:
    print(f"Received message: {msg.value().decode('utf-8')} at offset {msg.offset()}")

c.close()
