import requests
import time
import random
url = "http://swapi.co/api/people/1/"

json_result = requests.get(url).json()

films = json_result.get("films")

for film in films:
    film_result = requests.get(film).json()
    split_crawl = film_result["opening_crawl"].split("\r\n")
    for line in split_crawl:
        print(line)
        times = [.3, .1, 10, .5, .7, .04, .08, .001]
        part = random.randint(0,7)
        x = times[part]
        time.sleep(x)
