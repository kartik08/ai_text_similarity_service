from locust import HttpUser, task, between
import json
import random

class TextSimilarityUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def analyze_similarity(self):
        payload = {
            "prompt1": random.choice(["Hello world", "How are you Kartik", "This is a test runs"]),
            "prompt2": random.choice(["Hello again", "How do you do Kartik", "This test run is fine"]),
            "method": random.choice(["cosine", "jaccard"])
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/analyze", data=json.dumps(payload), headers=headers)
