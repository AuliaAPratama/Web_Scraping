from bs4 import BeautifulSoup
import requests
import csv

# lists of digimon
r = requests.get("https://wikimon.net/Visual_List_of_Digimon")
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find_all('table', class_='') # table yang tanpa class!
# print(len(data))        # 2-1280 data digimon
# print(data[2:1280])
# print(data[2].tr.find_next_sibling())
# print(data[2].tr.find_next_sibling().a.text)

DigimonData = []

for i in data[2:1280]:
        nama = i.tr.find_next_sibling().a
        gmbr1 = nama.find_parent()
        gmbr2 = gmbr1.find_parent()
        gmbr3 = gmbr2.find_parent()
        image = gmbr3.img['src']
        
        dataTarget = {
                'nama': nama.text,
                'gambar': 'https://wikimon.net'+image
        }
        DigimonData.append(dataTarget)


# save on csv
with open('6_digimon.csv', 'w', newline='', encoding='utf-8') as filedigi:
    kolom = ['nama', 'gambar']
    write = csv.DictWriter(filedigi, fieldnames=kolom)
    write.writeheader()
    write.writerows(DigimonData)