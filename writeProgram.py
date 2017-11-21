import urllib.request
from bs4 import BeautifulSoup
import os

url = "http://dbank.sakura.ne.jp/iphoneX.html"
response = urllib.request.urlopen(url)
rss = response.read().decode("utf-8")
soup = BeautifulSoup(rss, "xml")

name = 0
for s in soup.find_all("url"):
    name+=1
    download_image(name)

f = open('file.text', 'w')
f.writelines(rss)
f.close() 


