from os import link
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

import json

from shutil import which

chrome_options = Options()
# chrome_options.add_argument("--headless")

chrome_path = which("chromedriver.")

driver = webdriver.Chrome(executable_path = r'./chromedriver.exe', options=chrome_options)
driver.get('https://www.disco.com.uy/almacen/canasta-familiar')
driver.set_window_size(1800, 1000)


WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//w-div/span')))
pop_up = driver.find_element_by_xpath('//w-div/span')
pop_up.click()

pop_up_btn = driver.find_element_by_id('btnConfirmaSucursal')
pop_up_btn.click()

try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//w-div/span')))
    pop_up = driver.find_element_by_xpath('//w-div/span')
    pop_up.click()
except:
    print('Sin pop up nuevo')

links = []
links_productos = driver.find_elements_by_xpath('//div[@class="Product"]')
for product in links_productos:
    links.append(product.get_attribute('productid'))

driver.execute_script('window.scrollTo(0, 4500);')

next_page = True

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@id,"PagerBottom")]/ul/li[@class="next"]')))
next_page_button_link = driver.find_element_by_xpath('//div[contains(@id,"PagerBottom")]/ul/li[@class="next"]').click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@class="Product-image"]')))
print(next_page)
while next_page:
    driver.refresh()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="Product"]')))
    links_productos = driver.find_elements_by_xpath('//div[@class="Product"]')
    for product in links_productos:
        try:
            links.append(product.get_attribute('productid'))
        except:
            pass
    try:
        driver.execute_script('return window.scrollTo(0, 4500);')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@id,"PagerBottom")]/ul/li[@class="next"]')))
        next_page_button_link = driver.find_element_by_xpath('//div[contains(@id,"PagerBottom")]/ul/li[@class="next"]').click()
        print('click')
    except:
        print('Out')
        next_page = False

print(links)
print(len(links))

driver.close()

products_info = []

for link in links:
    url = f"https://www.disco.com.uy/api/catalog_system/pub/products/search/?fq=productId:{link}"
    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data = payload)
    products_info.append(json.loads(response.text))

print(products_info)

