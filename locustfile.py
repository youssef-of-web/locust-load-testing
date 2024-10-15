import json
import os
import random
from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        # Load configuration from JSON file
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_path) as f:
            self.config = json.load(f)

    @task
    def dynamic_request(self):
        for task in self.config['tasks']:
            if random.random() < task.get('weight', 1):
                url = task['url']
                method = task['method'].upper()
                headers = task.get('headers', {})
                body = task.get('body', {})

                if method == 'GET':
                    self.client.get(url, headers=headers)
                elif method == 'POST':
                    self.client.post(url, json=body, headers=headers)
                elif method == 'PUT':
                    self.client.put(url, json=body, headers=headers)
                elif method == 'DELETE':
                    self.client.delete(url, headers=headers)
                # You can add more methods as needed

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)