from locust import HttpUser, task, between

class StoryGenerationUser(HttpUser):
    wait_time = between(1, 2)  # Simulate a delay between requests

    @task
    def generate_story(self):
        self.client.post(
            "/generate_story",
            json={
                "prompt": "Once upon a time...",
                "max_length": 100,
                "temperature": 0.7,
                "mode": "fantasy"
            }
        )
