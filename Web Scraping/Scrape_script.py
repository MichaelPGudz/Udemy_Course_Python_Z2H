import time
import datetime
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


base_url = "https://www.x-kom.pl"
product_url = "https://www.x-kom.pl/g-7/c/2882-ubrania-dla-graczy.html"
product_data = {}
today = datetime.date.today()
month = today.strftime('%B')

def scrape_pages (product_url):
    i = 1
    shop_name = base_url.split('.')[1].strip()
    keys = ['name', 'url', 'price']
    product_data = dict.fromkeys(keys)
    shop_data = dict.fromkeys(shop_name)

    while True:
        result = requests.get(f"{product_url}?page={i}")
        soup = bs4.BeautifulSoup(result.text, "lxml")
        products = soup.select(".sc-1yu46qn-7")
        if products != []:
            for product in products:
                name = product.select("h3")[0].text
                print(name)
                price = product.select(".sc-6n68ef-3")[0].text
                url = base_url + product.select("a")[1]["href"]
                product_data['name'] = name
                product_data['price'] = {month: price}
                product_data['url'] = url
                shop_data[shop_name] = product_data
                print(len(shop_data['x-kom']))
                print(shop_data['x-kom'])
        else:
            break
        i += 1
    return shop_data

print(scrape_pages(product_url))
# PATH = r"C:\Users\Michael\chromedriver.exe"
# # PATH = r"C:\Users\GudzM\Downloads\chromedriver.exe"
#
# driver = webdriver.Chrome(PATH)
# driver.maximize_window()
# driver.get(base_url)
#
# landing_page = driver.find_elements_by_class_name("sc-13hctwf-3")
# land_lop = [element.text for element in landing_page]
# print(land_lop)
#
# n = 1
#
# shop_data = []
#
# for category_element in land_lop:
#     try:
#         category_link = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.LINK_TEXT, category_element))
#         )
#         category_link.click()
#         time.sleep(5)
#         category_page_sel = driver.find_elements_by_class_name("joe0ba-0")
#         category_lop = [element.text.split('(')[0].strip() for element in category_page_sel]
#         product_url = category_page_sel[n].get_attribute('href')
#         print(category_lop)
#         print(product_url)
#         for product_element in category_lop:
#             try:
#                 product_link = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, product_element))
#                 )
#                 product_link.click()
#                 product_page = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.TAG_NAME, "h1"))
#                 )
#                 print(f"I'm on a {product_page.text}")
#                 data = scrape_pages(product_url)
#                 shop_data.append(data)
#                 time.sleep(10)
#                 driver.back()
#                 print(shop_data)
#             except exceptions.StaleElementReferenceException as e:
#                 print(e)
#             finally:
#                 print(f"Finished for {product_element}")
#     except exceptions.StaleElementReferenceException as e:
#         print(e)
#     n += 1
#

#Landing Page

#List Elements class
# sc-1ktmy3g-2 -- list className

#Category List Elements
# sc-4wflom-1

#Category Element Class
# joe0ba-0 brNAIy sc-1h16fat-0 dEoadv

#Products list Id
# listing-container
