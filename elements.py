import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get('https://www.google.com')
googleSearchBox = driver.find_element(By.ID, "APjFqb")
driver.implicitly_wait(1)
googleSearchBox.send_keys("Automation")
driver.find_element(By.NAME, "btnK").click()


time.sleep(5)
driver.close()
driver.quit()
