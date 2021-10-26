# Load Testing

Collection of locust files

## Requirements

Install the required Python packages

```
pip install locust
pip install beautifulsoup4
pip install requests
pip install lxml
```

### homepage.py
Homepage only to any site

```
locust -f homepage.py
```

### wordpress.py
This would retrieve the sitemap and test the enlisted URL's

```
locust -f wodpress.py
```




