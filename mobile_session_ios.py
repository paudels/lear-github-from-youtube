from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, "TheAPP.app.zip")
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'PlatformVersion': '15',
    'deviceName': 'iPhone 14',
    'AutomationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS # it is not working so need some investigation around it

)
driver.quit()