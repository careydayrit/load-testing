# Author: Carey Dayrit
import time
import random

from locust import HttpUser, task, between
from pyquery import PyQuery

### HELPER FUNCTIONS Section
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    "Android 4.0.3;AppleWebKit/534.30;Build/IML74K;GT-I9220 Build/IML74K",
    "KWC-S4000/ UP.Browser/7.2.6.1.794 (GUI) MMP/2.0",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Googlebot-Image/1.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
]

class MyLocust(HttpUser):    	
    wait_time = between(1, 10)    
    
    def on_start(self): 
        self.headers = {
            "User-Agent":USER_AGENTS[random.randint(0,len(USER_AGENTS)-1)],
        }
        self.client.headers = self.headers
    
    @task
    def homepage(self, path="/"):
        # self.client.get("/", headers={"Cookie": "no-cache"})
        host=self.host
        r = self.client.get(path, headers={"Cookie": "no-cache"})
        pq = PyQuery(r.content)
        link_elements = pq("a")
        self.urls_on_current_page = [] # Pass the results into an array.
        # A loop reads the array and randomly picks a path 
        for l in link_elements:
            if "href" in l.attrib:
                url = l.attrib["href"]
                if url != "/user/logout":
                    # Ensure we only run links of the target site, excluding specific domains too
                    if url.startswith(host) or url.startswith('/'):
                        self.urls_on_current_page.append(l.attrib["href"])

        for u in self.urls_on_current_page:
            self.client.get(u)