import logging
from pyspark.sql import SparkSession

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        # Initialize Spark session
        spark = SparkSession.builder \
            .appName("KafkaSparkStreaming") \
            .getOrCreate()

        # Read streaming data from Kafka topic 'test-topic'
        df = spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka:9092") \
            .option("subscribe", "test-topic") \
            .option("startingOffsets", "earliest") \
            .load() \
            .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

        # Write streaming output to MinIO (S3A) as Parquet files
        query = df.writeStream \
            .format("parquet") \
            .option("path", "s3a://test-bucket/data") \
            .option("checkpointLocation", "s3a://test-bucket/checkpoint") \
            .trigger(processingTime="30 seconds") \
            .start()

        logging.info("Streaming job started.")
        query.awaitTermination()
    except Exception as e:
        logging.error(f"Streaming job failed: {e}")

if __name__ == "__main__":
    main()
