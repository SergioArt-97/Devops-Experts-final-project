FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Chrome + Selenium
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libgbm1 \
    libxcomposite1 \
    libxdamage1 \
    libxi6 \
    libappindicator3-1 \
    libdrm2 \
    libu2f-udev \
    xdg-utils \
    wget && \
    rm -rf /var/lib/apt/lists/*

# Download and install Chromium
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV CHROME_BIN=/usr/bin/google-chrome

# Install Python deps
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . /app

# Expose port
EXPOSE 8777

# Run your Flask app
CMD ["python3", "MainScores.py"]
