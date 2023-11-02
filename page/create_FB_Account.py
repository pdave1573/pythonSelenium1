import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class create_AC:
    driver = webdriver.Chrome()
    driver.maximize_window()

    birth_month = driver.find_element(By.XPATH, ".//select[@name='birthday_month']")
    sex_male = driver.find_element(By.XPATH,".//input[@name='sex' and @value='2']")

    sel = Select(birth_month)
    sel.select_by_value("3")

    sex_male.click()
    time.sleep(10)