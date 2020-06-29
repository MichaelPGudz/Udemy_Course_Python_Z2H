import requests
import bs4

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

n = 1
two_star_titles = {}

for page in range(1, 51):
    site_page = base_url.format(page)
    res = requests.get(site_page)

    soup = bs4.BeautifulSoup(res.text, "lxml")

    books = soup.select(".product_pod")
    two_star_titles.update({f"Page {n}": []})

    for book in books:
        if book.select(".star-rating.Two") != []:
            book_title = book.select('a')[1]['title']
            two_star_titles[f"Page {n}"].append(book_title)
    n += 1
print("Books with 2 star rating: ", two_star_titles, sep="\n")