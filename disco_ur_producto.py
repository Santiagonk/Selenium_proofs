from os import link
from selenium import webdriver
import selenium

import requests

import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from shutil import which

chrome_options = Options()
# # chrome_options.add_argument("--headless")

# chrome_path = which("chromedriver.")

driver = webdriver.Chrome(executable_path = r'./chromedriver.exe', options=chrome_options)
driver.get('https://www.disco.com.uy/api/catalog_system/pub/products/search/?fq=productId:13124')
driver.set_window_size(1800, 1000)


# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//w-div/span')))
# pop_up = driver.find_element_by_xpath('//w-div/span')
# pop_up.click()

# pop_up_btn = driver.find_element_by_id('btnConfirmaSucursal')
# pop_up_btn.click()

# try:
#     WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//w-div/span')))
#     pop_up = driver.find_element_by_xpath('//w-div/span')
#     pop_up.click()
# except:
#     print('Sin pop up nuevo')


# name = driver.find_element_by_xpath('//div[@class="contenedorUndidadesPrecios"]//div[@class="Product-head"]/h3/a')
# brand = driver.find_element_by_xpath('//div[@class="contenedorUndidadesPrecios"]//div[@class="Product-head"]/h3/div')
# price_complete = driver.find_element_by_xpath('//div[contains(@class,"descripcion-producto")]//div[@class="Product-price"]/span')
# try:
#     price_discount = driver.find_element_by_xpath('//div[contains(@class,"descripcion-producto")]//div[@class="Product-promo-price"]/span[@class="santander-promo-price"]')
#     price_discount = price_discount.text
# except:
#     price_discount = ""
# unit = driver.find_element_by_xpath('//div[contains(@class,"descripcion-producto")]//span[@id="tag-unidades"]')
# base_quantity = driver.find_element_by_xpath('//div[contains(@class,"descripcion-producto")]//div[@class="Multiplier listing"]/div')
# category = driver.find_element_by_xpath('//li[@class="last"]//span[@itemprop="name"]')
# description = driver.find_element_by_xpath('//div[@class="productDescription"]')
# image_path = driver.find_element_by_xpath('//img[@id="image-main"]')

# print(name.text)
# print(brand.text)
# print(price_complete.text)
# print(price_discount)
# print(unit.text)
# print(base_quantity.text)
# print(category.text)
# print(description.text)
# print(image_path.get_attribute('src'))

# driver.close()

# url = f"https://www.disco.com.uy/api/catalog_system/pub/products/search/?fq=productId:13124"
# payload = {}
# headers = {}



# response = requests.get(url, headers=headers, data = payload)
# products_info.append(json.loads(response.text))