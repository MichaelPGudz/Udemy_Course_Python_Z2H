import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")
first_image = soup.select(".thumbimage")[0]
first_image_binary = first_image["src"]

image_link = requests.get(f"https:{first_image_binary}")
# image_link.content
file = open('Deep_Blue.jpg', 'wb')
file.write(image_link.content)
file.close()