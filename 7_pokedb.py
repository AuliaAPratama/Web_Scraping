from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://pokemondb.net/pokedex/all')
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find_all('td', class_='cell-num cell-fixed')
# print(len(data))

PokemonData = []
for i in data:
    index_poke = i.text
    pict_poke = i.span.span['data-src']
    nama_poke = i.find_next_sibling().a.string
    tipe_poke = i.find_next_sibling().find_next_sibling().a.string

    dataTarget = {
        'index': index_poke,
        'nama': nama_poke,
        'tipe': tipe_poke,
        'image': pict_poke
    }
    PokemonData.append(dataTarget)


# save on csv
with open('7_pokedb.csv', 'w', newline='', encoding='utf-8') as filepoke:
    kolom = ['index', 'nama', 'tipe', 'image']
    write = csv.DictWriter(filepoke, fieldnames=kolom)
    write.writeheader()
    write.writerows(PokemonData)
