import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'drivers', 'chromedriver.exe'))
driver = webdriver.Chrome(service=service)
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID, 'account').send_keys('test01')
time.sleep(1)
driver.find_element(By.NAME, 'password').send_keys('newdream123')
time.sleep(1)
driver.find_element(By.ID, 'submit').click()
time.sleep(1)

driver.find_element(By.XPATH, '//a/span[text()=" 我的地盘"]').click()
time.sleep(1)
driver.find_element(By.ID, 'userNav').click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="/zentao/www/index.php?m=user&f=logout"]').click()
time.sleep(1)




