# ambil data power ranger, mulai siaran & akhir siaran

from bs4 import BeautifulSoup
import requests

# lists of power rangers
r = requests.get("https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes")
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find(class_='wikitable').tbody
for i in data.find_all('i'):
    if 'Rangers' in i.text:
        parent = i.find_parent()
        sibling = parent.find_next_siblings()
        dateStart = sibling[1].find('span', class_='bday dtstart published updated')
        dateEnd = sibling[2].find('span', class_='dtend')
        print(i.text, ' || ', dateStart.text, ' || ', dateEnd.text)
    else :
        print("Sorry we can't find something that you're looking for")

