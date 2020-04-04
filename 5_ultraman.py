from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
soup = BeautifulSoup(r.content, 'html.parser')
strong = soup.find_all('strong')

UltramanData = []
for i in strong:
    UltramanData.append(i.text)
ultra = UltramanData[2:36]
monster = UltramanData[37:110]

print(ultra)
print(monster)