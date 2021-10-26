# Author: Carey Dayrit
from locust import HttpUser, task, between
from bs4 import BeautifulSoup
import time
import requests

class MyLocust(HttpUser):    	
    wait_time = between(1, 10)    
    
    @task
    def homepage(self):
        self.client.get("/", headers={"Cookie": "no-cache"})

    @task(1)
    def sitemap(self):
        host=self.host
        url=host + "/wp-sitemap.xml"
        soup=BeautifulSoup(requests.get(url).text, 'lxml')
        for loc in soup.select('sitemap > loc'):
            subxml=loc.text[len(host):]
            suburl = host + subxml
            subsoup = BeautifulSoup(requests.get(suburl).text, 'lxml')
            for subloc in subsoup.select('url > loc'):
                subdirectory=subloc.text[len(host):]                
                self.client.get(subdirectory, headers={"Cookie": "no-cache"})