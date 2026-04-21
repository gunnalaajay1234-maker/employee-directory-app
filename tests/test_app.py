from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def test_add_employee():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.binary_location = "/usr/bin/chromium-browser"
    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("http://localhost:5000")  # replace with EC2 IP if needed

    input_box = driver.find_element(By.NAME, "employee")
    input_box.send_keys("Ajay")

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(2)

    assert "Ajay" in driver.page_source

    driver.quit()