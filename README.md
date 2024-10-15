# Locust Load Tasting

### What is Locust?

Locust is an open-source load testing tool that allows you to define user behavior with Python code and run tests to simulate thousands of concurrent users. It provides a web-based user interface for monitoring the load test in real time.

### Prerequisites

- Docker installed on your machine.
- Basic knowledge of how to use Docker.

### Launch Locust

```
docker-compose up -d 
```

### Launch Locust with scalable workers

```
docker-compose up -d --scale worker=NB-OF-WORKERS

```