import requests
from bs4 import BeautifulSoup

tuckahoe = requests.get("https://www.tuckahoeschools.org")
soup = BeautifulSoup(tuckahoe.text )