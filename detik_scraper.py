import requests
from bs4 import BeautifulSoup

html_sorce = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar' })
print(html_sorce)

soup = BeautifulSoup(html_sorce.text,'html.parser')
populer_area = soup.find(attrs={'class':'grid-row list-content'})
# Menangkap Judulnya Saja pada Artikel
titles = populer_area.findAll(attrs={'class':'media__title'})
images = populer_area.findAll(attrs={'class':'media__image'})

# Menangkap Hanya Judulnya Saja Tanpa HTML
for title in titles:
    print(title.text)

# menangkap Image dan Title
for image in images:
    print(image.find('a').find('img')['title'])

@app.route('')
def home():
    return render_template('index.html')
@app.route('/detik-populer')
def detik_populer:
    html_sorce = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar'})
    print(html_sorce)
    soup = BeautifulSoup(html_sorce.text, 'html.parser')
    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    # Menangkap Judulnya Saja pada Artikel
    titles = populer_area.findAll(attrs={'class': 'media__title'})
    images = populer_area.findAll(attrs={'class': 'media__image'})
