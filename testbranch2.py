from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/chromedriver2.exe')

driver = webdriver.Chrome(service=s)

driver.get('https://yandex.ru/')

element = driver.find_element(By.ID, 'text')\

element.send_keys('Russia')

element2 = driver.find_element(By.CLASS_NAME, 'search2__button')
element2.click()

element3 = driver.find_element(By.XPATH, '/html/body/header/div/div/div[4]/div[3]/a[2]')
element3.click()

driver.quit()
