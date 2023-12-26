from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import os

url="https://www.saucedemo.com/"

def open_page():
    driver_path=Service(executable_path=os.getcwd()+"\chromeDriver\chromedriver.exe")  #fetching the chromedriver.exe file location 
    driver=Chrome(service=driver_path)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    return driver

