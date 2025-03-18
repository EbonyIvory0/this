import json
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.get("https://app.staging.sphera.work/")
    driver.maximize_window()
    yield driver  # Возврат драйвера тесту
    # Завершение работы после всех тестов
    driver.quit()

