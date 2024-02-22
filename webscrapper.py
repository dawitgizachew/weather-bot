# pip install bs4pip install bs4
# pip install requests

import requests
from bs4 import BeautifulSoup
url = 'https://www.timeanddate.com/weather/ethiopia/addis-ababa'

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("div", class_="bk-focus__info")

title = post.find("dev", class_="h2").text.strip()
print(title)
