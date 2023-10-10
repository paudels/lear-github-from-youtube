import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.dominos.com')
time.sleep(5)
driver.close()
driver.quit()



# driver.get('https://www.dominos.com')
# time.sleep(5)




