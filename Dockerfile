# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Install necessary dependencies for your application
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    chromium \
    chromium-driver

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose port 8777 for Flask app
EXPOSE 8777

# Set environment variables for headless Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromium-driver

# Run the Flask app (adjust this if the entry file is different)
CMD ["python3", "MainScores.py"]
