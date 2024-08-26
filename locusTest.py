from locust import HttpUser, between, task
from data.data import Data


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def get_pet_info(self):
        self.client.get("/v2/pet/3432")

    @task
    def pet_create(self):
        self.client.post("/v2/pet", json=Data.pet_create_payload())

    @task
    def update_pet(self):
        self.client.put("/v2/pet", json=Data.pet_update_payload())

    @task
    def user_delete(self):
        self.client.delete("/v2/pet/3432")
