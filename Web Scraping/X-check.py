import time
import requests
import lxml
import bs4

sites = []
for number in range(406961, 406970):
    kom = "https://www.x-kom.pl/p/"
    kom += str(number)
    sites.append(kom)

x_kom_prices = {}

for site in sites:
    time.sleep(5)
    soup = requests.get(site)
    x_kom = bs4.BeautifulSoup(soup.text, "lxml")
    try:
        price_value = x_kom.select(".u7xnnm-4")[0].getText()
        name = x_kom.select("h1")[0].getText()
    except:
        name = "Product doesn't Exist"
        price_value = "No price"
    x_kom_prices.update({site: [name, soup.status_code, price_value]})


print(x_kom_prices)

