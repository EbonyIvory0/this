import json
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.get("https://app.staging.sphera.work/")
    driver.maximize_window()
    with open("cookies.json", "r", encoding="utf-8") as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
        driver.refresh()
    yield driver  # Возврат драйвера тесту
    # Завершение работы после всех тестов
    driver.quit()

