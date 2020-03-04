import os
import string
import random

from locust import HttpLocust, TaskSet, task, between

class MyTaskSet(TaskSet):
	@task
	def index(self):
		response = self.client.get("/")
        
class MyLocust(HttpLocust):
	task_set = MyTaskSet
	wait_time = between(1, 10)
