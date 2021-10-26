# Author: Carey Dayrit
import time

from locust import HttpUser, task, between
     
class MyLocust(HttpUser):    	
    wait_time = between(1, 10)    
    
    @task
    def homepage(self):
        self.client.get("/", headers={"Cookie": "no-cache"})
        
