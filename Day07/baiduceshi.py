

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Administrator\Desktop\1\chromedriver.exe")

driver.get("https://www.baidu.com")

driver.maximize_window()
driver.find_element(By.ID,"kw").send_keys("GPT")
driver.find_element(By.ID,"su").click()
time.sleep(70)