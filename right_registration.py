import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/registration2.html"

first_name_field = "input[placeholder='Input your first name']"
last_name_field = "input[placeholder='Input your last name']"
e_mail_field = "input[placeholder='Input your email']"
submit_button = "//button[text()='Submit']"

try:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(link)

    first_name_field = driver.find_element_by_css_selector(first_name_field)
    last_name_field = driver.find_element_by_css_selector(last_name_field)
    e_mail_field = driver.find_element_by_css_selector(e_mail_field)
    submit_button = driver.find_element(By.XPATH, submit_button)

    first_name_field.send_keys("Orpi")
    last_name_field.send_keys("Piupe")
    e_mail_field.send_keys("zimail")
    submit_button.click()

    time.sleep(1)

    assert driver.find_element_by_tag_name("h1").text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    driver.quit()
