from seleniumTest.selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("https://www.google.com")

title = driver.title
