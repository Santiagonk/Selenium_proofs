from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from shutil import which

chrome_options = Options()
# chrome_options.add_argument("--headless")

chrome_path = which("chromedriver.")

driver = webdriver.Chrome(executable_path = r'./chromedriver.exe', options=chrome_options)
driver.get('https://www.disco.com.uy/?sc=4')
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

categories_dropdown = driver.find_element_by_xpath('//div[@id = "menuDesktop"]/i[contains(@class,"chevron-down")]')
categories_dropdown.click()

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'contenedor-Categs-desktop')))
categories_select = driver.find_elements_by_xpath('//*[@id="contenedor-Categs-desktop"]/nav/ul/li/a')
# nav_bar = driver.find_element_by_class_name('list-group list-group-flush menu-desktop')
categories = []
for category in categories_select:
    categories.append(category.text)

subcategories = []
x = 0

for i in range(1, 24):
    almacen = driver.find_element_by_xpath(f'//*[@id="contenedor-Categs-desktop"]/nav/ul/li[{i}]').click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'list-group')))
    # nav_bar.location_once_scrolled_into_view
    # driver.execute_script(f'return arguments[0].scrollTo({x},{x+100});', nav_bar)
    print('The scraping for the ',i,' element')
    x +=100
    subcategories_select = driver.find_element_by_xpath(f'//*[@id="item-{i-1}"]/h5/a')
    subcategories.append(subcategories_select.get_attribute('href'))


# for category in subcategories_select:
#             subcategories.append(category.text)
print(categories)
print(subcategories)

# categories_select.click()
# print(categories_select)

# for i in range(1,23):
#     item = driver.find_element_by_xpath(f'//*[@id="contenedor-Categs-desktop"]/nav/ul/li[{i}]/a/')
#     item.

# categories_list = driver.find_elements_by_xpath('//ul[contains(@class,"list-group")]/li/a/text()').getall()
# print(categories_list)


# search_input.send_keys('My User Agent')

# search_btn = driver.find_element_by_id('search_button_homepage')
# search_btn.click()

# search_input.send_keys(Keys.ENTER)

#print(driver.page_source)

# driver.close()