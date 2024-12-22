from locust import HttpUser, task, between

class StoryGenerationUser(HttpUser):
    host = "https://vespera-ai-backend.vercel.app/"  # Set the base URL of your deployed API
    wait_time = between(1, 2)  # Random wait time between 1 to 2 seconds between requests

    @task(2)  # Task weight: will be executed twice as often as check_health
    def generate_story(self):
        response = self.client.post(
            "/generate_story",  # The endpoint to send the request to
            json={
                "prompt": "Once upon a time...",
                "max_length": 100,
                "temperature": 0.7,
                "mode": "fantasy"
            }
        )

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            print("Story generated successfully!")
        else:
            print(f"Failed with status code {response.status_code}. Response: {response.text}")

    @task(1)  # Task weight: will be executed half as often as generate_story
    def check_health(self):
        response = self.client.get("/health")  # Endpoint to check the health status of the app
        
        # Check if the health check returns a successful response
        if response.status_code == 200:
            print("Health check passed.")
        else:
            print(f"Health check failed with status code {response.status_code}")
