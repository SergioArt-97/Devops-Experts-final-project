FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask selenium webdriver-manager \
    && apt-get update && apt-get install -y curl

EXPOSE 5000

CMD ["python", "MainScores.py"]
