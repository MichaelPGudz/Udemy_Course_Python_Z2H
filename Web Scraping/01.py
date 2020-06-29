import requests
# import lxml
import bs4


result = requests.get("https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction")
# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

print(soup.select("h2")[0].getText())

site_paragrpahs = soup.select("p")
print(site_paragrpahs[0].getText())