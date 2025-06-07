FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application source code
COPY src/app.py .
COPY connector-config/connector-config.json ./connector-config/
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the app
CMD ["python", "app.py"]