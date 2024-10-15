# Locust Load Testing

<img src="/images/screen.png">

## What is Locust?

Locust is an open-source load testing tool that allows you to define user behavior with Python code and run tests to simulate thousands of concurrent users. It provides a web-based user interface for monitoring the load test in real time.

## Prerequisites

- Docker installed on your machine.
- Basic knowledge of how to use Docker.

## Locust Load Testing Configuration

This README provides instructions on how to configure and use the `config.json` file for your Locust load testing setup.

### Overview

The `config.json` file allows you to define dynamic tasks for your load tests, including various HTTP methods, request URLs, request bodies, and headers. This enables flexible and easy adjustments to your load testing scenarios without modifying the Python code.

### Structure of `config.json`

The configuration file is structured as a JSON object with an array of tasks. Each task can include the following fields:

- **url**: The endpoint to which the request will be made (required).
- **method**: The HTTP method to use for the request (GET, POST, PUT, DELETE) (required).
- **weight**: A numerical value that determines the relative frequency of the task being executed (optional, default is 1).
- **body**: A JSON object representing the request body for POST and PUT methods (optional).
- **headers**: A JSON object representing the headers to include in the request (optional).

### Example Configuration

Here’s an example of a `config.json` file:

```json
{
    "tasks": [
        {
            "url": "/",
            "method": "GET",
            "weight": 2,
            "headers": {
                "Authorization": "Bearer your_token"
            }
        },
        {
            "url": "/api/resource",
            "method": "POST",
            "weight": 1,
            "body": {
                "key": "value",
                "another_key": "another_value"
            },
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer your_token"
            }
        },
        {
            "url": "/api/resource/1",
            "method": "PUT",
            "weight": 1,
            "body": {
                "key": "updated_value"
            },
            "headers": {
                "Content-Type": "application/json",
                "Authorization": "Bearer your_token"
            }
        },
        {
            "url": "/api/resource/1",
            "method": "DELETE",
            "weight": 1,
            "headers": {
                "Authorization": "Bearer your_token"
            }
        }
    ]
}
```

### Run Locust

```
docker-compose up -d 
```

### Run Locust with scalable workers

```
docker-compose up -d --scale worker=NB-OF-WORKERS

```
