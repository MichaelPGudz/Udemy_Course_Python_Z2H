import requests
import bs4

result = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text, "lxml")

def authors_list() :
    authors = soup.select(".author")
    return set(author.text for author in authors)

print(authors_list())

def quote_list():
    quotes = soup.select(".text")
    return [quote.text for quote in quotes]

print(quote_list())

def tag_list():
    tags = soup.select(".tag-item")
    anchor_tags = []

    for tag in tags:
        anchor_tags += tag.select("a")

    return [tag.text for tag in anchor_tags]

print(tag_list())

def site_pages ():
    unique_authors = set()
    n = 1
    while True:
        quotes_to_scrape = requests.get(f"http://quotes.toscrape.com/page/{n}/")
        soup = bs4.BeautifulSoup(quotes_to_scrape.text, "lxml")
        authors = soup.select(".author")
        if authors != []:
            for author in authors:
                unique_authors.add((author.text))
        else:
            break
        n += 1
    return unique_authors

print(site_pages())
print(len(site_pages()))
