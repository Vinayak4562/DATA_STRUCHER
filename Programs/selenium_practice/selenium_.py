from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(executable_path="D:\\DRIVERS\\chromedriver_win32\\chromedriver.exe")

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://app.keka.com/Account/Login")

driver.maximize_window()
print(driver.title)
# driver.close()
