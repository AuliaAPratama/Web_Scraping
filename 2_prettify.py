### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup

### from html file:
soup = BeautifulSoup(open('contoh.html', 'r'), 'html.parser')
# print(soup)
print(soup.prettify())