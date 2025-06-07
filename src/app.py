import json

def read_file_and_send_to_topic(file_path, topic):
    """
    Reads a file line by line and (simulated) sends each line to the specified topic.
    Replace the print statement with actual Kafka producer logic as needed.
    """
    with open(file_path, 'r') as file:
        for line in file:
            # TODO: Replace this print with actual Kafka producer send logic
            print(f"Sending to {topic}: {line.strip()}")

if __name__ == "__main__":
    # Path to the connector configuration file
    config_path = '../connector-config/connector-config.json'
    
    # Load configuration from JSON file
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    
    # Extract file path and topic from config
    file_path = config['config']['file']
    topic = config['config']['topic']
    
    # Process the file and send lines to the topic
    read_file_and_send_to_topic(file_path, topic)