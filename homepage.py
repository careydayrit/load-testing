# Author: Carey Dayrit
# Description: Homepage without cache

import time

from locust import HttpUser, task, between
     
class MyLocust(HttpUser):    	
    wait_time = between(1, 10)    
    
    @task
    def homepage(self):
        self.client.get("/", headers={"User-Agent":"python-requests/2.6.0 CPython/2.7.5 Linux/3.10.0-862.14.4.el7.x86_64", "Cookie": "no-cache"})
        
