import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    email = driver.find_element(By.XPATH,".//*[@aria-label='Email or phone number']")
    password = driver.find_element(By.XPATH,".//*[@aria-label='Password']")
    login_btn = driver.find_element(By.XPATH,".//*[@name='login']")
    create_AC_btn = driver.find_element(By.XPATH,"(.//a[@role='button'])[2]")

    email.clear()
    email.send_keys("test324534565128766")

    password.clear()
    password.send_keys("Test")

    login_btn.click()
    time.sleep(10)
    driver.back()

