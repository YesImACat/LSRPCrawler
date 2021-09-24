import datetime
import requests
from bs4 import BeautifulSoup

now = datetime.datetime.now()

url = 'https://forum.ls-rp.io/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

who_is = soup.find("div", class_="stat-block online-list")
print(who_is.get_text())
username = who_is.find_all("a", class_="username")

f=open(str(now), "w+")
for username in username:
    f.write(username.get_text() + "\n")

f.close()