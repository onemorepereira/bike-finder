from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tabulate import tabulate
import logging
import yaml

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

with open("stores.yml", 'r') as stream:
    try:
        STORES = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        logging.error("Error loading YAML from stores.yml")

bikes = []

opts = Options()
opts.headless=True
driver = webdriver.Firefox(options=opts)

for store in STORES:
    logging.info('{} - scraping'.format(store[0]))
    driver = webdriver.Firefox(options=opts)
    try:
        driver.get(store[3])
        products = driver.find_elements_by_class_name(store[1]) #returns available bike models
        prices   = driver.find_elements_by_class_name(store[2]) #return available bike prices
        logging.info('{} - found {} bikes'.format(store[0], len(products)))
        for product, price in zip(products, prices):
            bikes.append({'store': store[0], 'name': product.text.replace('\n',' ').upper(), 'price': price.text.replace(',','')})
    except:
        logging.error('{}'.format(store[0]))
    finally:
        products = None
        prices   = None
        driver.quit()

table = tabulate(sorted(bikes, key = lambda i: i['store']), headers="keys", tablefmt="simple")
print(table)

driver.quit()