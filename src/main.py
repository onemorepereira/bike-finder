from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tabulate import tabulate

URL_BIKEMART  =['BIKEMART',  'https://www.bikemart.com/product-list/bikes-1000/?&rb_av=instore&rb_ct=1008&rb_sz=Large']
URL_JENSONUSA =['JENSONUSA', 'https://www.jensonusa.com/Mountain-Bikes?WheelSize=29%22&Gender=Men&Size=Large&MultiValueIntendedUse=Trail+%2f+All-Mountain']
URL_CADENCE   =['CADENCE',   'https://www.cadencecyclery.com/product-list/bikes-1000/mountain-1006/?rb_av=instore&rb_ct=1008&rb_sz=Large']

bikes = []

opts = Options()
opts.headless=True
driver = webdriver.Firefox(options=opts)

# JENSON USA
driver.get(URL_JENSONUSA[1])
products = driver.find_elements_by_class_name('product-name') #returns available bike models
prices   = driver.find_elements_by_class_name('product-price-saleprice') #return available bike prices
for product, price in zip(products, prices):
    bikes.append({'store': URL_JENSONUSA[0], 'name': product.text, 'price': price.text})

# BIKEMART
driver.get(URL_BIKEMART[1])
products = driver.find_elements_by_class_name('seProductTitle') #returns available bike models
prices   = driver.find_elements_by_class_name('seRegularPrice') #return available bike prices
for product, price in zip(products, prices):
    bikes.append({'store': URL_BIKEMART[0], 'name': product.text.replace('\n', ' ').upper(), 'price': price.text})

# BIKEMART
driver.get(URL_CADENCE[1])
products = driver.find_elements_by_class_name('seProductTitle') #returns available bike models
prices   = driver.find_elements_by_class_name('seRegularPrice') #return available bike prices
for product, price in zip(products, prices):
    bikes.append({'store': URL_CADENCE[0], 'name': product.text.replace('\n', ' ').upper(), 'price': price.text})
    

# for bike in sorted(bikes, key = lambda i: i['name']):
#     print(bike)
table = tabulate(sorted(bikes, key = lambda i: i['name']), headers="keys", tablefmt="simple")
print(table)

driver.quit()