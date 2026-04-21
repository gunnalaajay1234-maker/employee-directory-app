from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_add_employee():
    driver = webdriver.Chrome()

    driver.get("http://localhost:5000")  # or your EC2 IP

    driver.find_element(By.NAME, "employee").send_keys("Ajay")
    driver.find_element(By.TAG_NAME, "button").click()

    assert "Ajay" in driver.page_source

    driver.quit()
