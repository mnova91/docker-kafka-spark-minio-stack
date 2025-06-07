# docker-connector-app/docker-connector-app/README.md

# Docker Connector Application

This is a **personal project** for learning and experimentation with Docker, Kafka, Spark, and MinIO.  
**Use with care:** This repository is provided as-is, without any warranty. It is intended for educational and development purposes only.

## Project Structure

```
docker-kafka-spark-minio-stack
├── src
│   ├── app.py                # Main application script
│   ├── producer.py           # Kafka producer example
│   ├── consumer.py           # Kafka consumer example
│   ├── streaming_job.py      # Spark streaming job
│   └── index.js              # Node.js connector example
├── connector-config.json     # Kafka connector configuration
├── s3-sink-connector.json    # S3/MinIO sink connector config
├── Dockerfile                # Dockerfile for building the image
├── requirements.txt          # Python dependencies
├── docker-compose.yaml       # Multi-service stack
├── .env.example              # Example environment variables (no secrets)
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd docker-kafka-spark-minio-stack
   ```

2. **Copy and edit environment variables:**
   ```sh
   cp .env.example .env
   # Edit .env to set your own credentials (do NOT commit your real .env)
   ```

3. **Build and run the stack:**
   ```sh
   docker-compose up --build
   ```

4. **Access services:**
   - Kafka UI: [http://localhost:8085/](http://localhost:8085/)
   - MinIO: [http://localhost:9000/](http://localhost:9000/) (console at :9001)
   - Spark UI: [http://localhost:8080/](http://localhost:8080/)
   - Kafka Connect: [http://localhost:8083/](http://localhost:8083/)

## Usage

- The application reads from the file specified in `connector-config.json` and sends the data to the topic defined in the same configuration file.
- Example producer and consumer scripts are provided in `src/`.
- The Spark streaming job reads from Kafka and writes to MinIO as Parquet files.
- **Ensure that any file paths in configs are accessible from within the Docker containers.**

## Dependencies

All Python dependencies are listed in `requirements.txt`.  
Install them with:
```sh
pip install -r requirements.txt
```
Other dependencies (Node.js, Docker, etc.) are noted in the relevant files.

## License

This project is licensed under the MIT License.

---

**Disclaimer:**  
This is a personal project and not intended for production use.  
Use at your own risk.  
No sensitive data or credentials are included in this repository.