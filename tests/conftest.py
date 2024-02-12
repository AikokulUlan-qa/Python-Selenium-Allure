'''
Configuration test
'''
# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
                
# каждый тест должен начинаться с test_ , здесь мы должны запустить и настроить браузер
def browser():
    """
    Main fixture
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    chrome_options.add_argument("--disable-gpu")#applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage")#overcome limited resource problems
    # chrome_options.add_argument("--headless") # спец. режим "без браузера" # этот режим нужен когда хром и браузер тяжело загружаются, тест проводится без него
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
	
    yield driver
    driver.quit()	
    
   