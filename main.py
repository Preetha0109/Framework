


from selenium import webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()

a = 'wdwdw'
driver.find_element(By.XPATH, a).send_keys()