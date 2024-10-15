from locust import HttpUser, TaskSet, task, between, SequentialTaskSet
import random

class UserBehavior(TaskSet):

    @task(1)  # This task has twice the weight
    def index(self):
        self.client.get("/")

#    @task(2)
#    def post_request(self):
#        self.client.post("/api/resource", json={"key": "value"})

#    @task(3)
#    def put_request(self):
#        self.client.put("/api/resource/1", json={"key": "new_value"})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)