# импортируем модули и отдельные классы
import pytest

from selenium.webdriver.common.by import By

# каждый тест должен начинаться с test_ , здесь мы должны запустить и настроить браузер
def test_product_view_sku(browser):
    """
    Test case WERT-1
    """
		
    # определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    browser.get(url=url)
		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'BFB9ZOK210', "Unexpected sku"
    
  

   
 
 