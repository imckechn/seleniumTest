from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "./chromedriver"

def automator():
    driver = webdriver.Chrome(PATH)

    driver.get("https://techwithtim.net")

    print(driver.title)

    search = driver.find_element(By.NAME, "s")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)

    header = driver.find_element(By.ID, "menu-item-2262")
    header.click()

    print(driver.page_source)

automator()