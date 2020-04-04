from bs4 import BeautifulSoup
import requests
import csv

# lists of digimon
url = 'http://digidb.io/digimon-list/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.find_all('tr')[1])

# print results
# <tr>
# <td width="5%"><b> 1</b></td><td width="21%"> 
# <img src="http://digidb.io/images/dot/dot629.png" style="vertical-align:middle;"> 
# <a href="http://digidb.io/digimon-search/?request=1" style="font-weight: bold;">Kuramon</a>
# </img>
# </td>
# <td width="9%"><center>Baby</center></td>
# <td width="7%"><center>Free</center></td>
# <td width="7%"><center>Neutral</center></td>
# <td width="7%"><center>2</center></td>
# <td width="8%"><center>0</center></td>
# <td><center>590</center></td>
# <td><center>77</center></td>
# <td><center>79</center></td>
# <td><center>69</center></td>
# <td><center>68</center></td>
# <td><center>95</center></td>
# </tr>

DigidbData = []
for i in soup.find_all('tr')[1:]:
        no = i.find('td', width='5%').text
        nama = i.a.text
        image = i.img['src']
        stage = i.find('td', width='9%').text
        tipe = i.find('td', width='7%').text
        attr = i.find('td', width='7%').find_next_sibling().text
        memory = i.find('td', width='7%').find_next_sibling().find_next_sibling().text
        equipSlot = i.find('td', width='8%').text
        HP = i.find('td', width='8%').find_next_sibling().text
        SP = i.find('td', width='8%').find_next_sibling().find_next_sibling().text
        ATK = i.find('td', width='8%').find_next_sibling().find_next_sibling().find_next_sibling().text
        DEF = i.find('td', width='8%').find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text
        INT = i.find('td', width='8%').find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text
        SPD = i.find('td', width='8%').find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text

        dataTarget = {
               'No': int(no),
               'Nama': nama,
               'Image': image,
               'Stage': stage,
               'Tipe': tipe,
               'Attr': attr,
               'Memory': memory,
               'EquipSlot': equipSlot,
               'HP': HP,
               'SP': SP,
               'ATK': ATK,
               'DEF': DEF,
               'INT': INT,
               'SPD': SPD
        }
        DigidbData.append(dataTarget)

# print(DigidbData[0])
# print(list(DigidbData[0].keys()))


# save to csv
with open('8_digidb.csv', 'w', newline = '') as digidbfile:
    kolom = list(DigidbData[0].keys())
    tulis = csv.DictWriter(digidbfile, fieldnames = kolom)
    tulis.writeheader()
    tulis.writerows(DigidbData)