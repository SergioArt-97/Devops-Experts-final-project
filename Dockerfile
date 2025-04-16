FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install only essential dependencies
RUN apt-get update && apt-get install -y python3-pip

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 5000

# Run the app
CMD ["python3", "MainScores.py"]
