import requests
import time
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

search_url = "http://search.azlyrics.com/search.php?q="
artist = "dean+martin"
body = requests.get(search_url + artist)
souper = BeautifulSoup(body.text, 'html.parser')


all_a_tags = souper.findAll('a')
next_page = all_a_tags[28].get("href")


body = requests.get(next_page, headers=headers)
souper = BeautifulSoup(body.text, 'html.parser')
all_a_tags = souper.findAll('a')[32:496]
song_link_list = []

for counter, tag in enumerate(all_a_tags):
    if not tag.get('rel') and tag.get('href'):
        song_link_list.append(tag.get("href"))
for x in song_link_list:
    new_song_link = x.replace("..", "http://azlyrics.com")
    song_page = requests.get(new_song_link, headers=headers)
    souper = BeautifulSoup(song_page.text, 'html.parser')
    song_divs = souper.findAll('div')[22]
    print(song_divs.text)


    input()
