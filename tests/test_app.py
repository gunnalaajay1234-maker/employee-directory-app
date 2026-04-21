from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_add_employee():
    # Setup ChromeDriver correctly
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:5000")

    driver.find_element(By.NAME, "employee").send_keys("Ajay")
    driver.find_element(By.TAG_NAME, "button").click()

    assert "Ajay" in driver.page_source

    driver.quit()
