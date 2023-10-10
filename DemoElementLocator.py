import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https:www.dominos.com")

driver.implicitly_wait(1)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/button").click()
driver.find_element(By.XPATH, '//*[@id="__next"]/header/div/nav/ul[2]/li[2]/button').click()
# time.sleep(1)
driver.find_element(By.ID, "Email"). send_keys("sunil.paudel@dominos.com")
driver.find_element(By.ID, "Password"). send_keys("Passw0rd1")
driver.find_element(By.CSS_SELECTOR, "button[data-quid='sign-in-button']").click()
time.sleep(5)

# doesn't work now because of the initial pop up on homepage




