import time
from selenium.webdriver.common.by import By


def test_basket_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    add_basket_button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert len(add_basket_button) <= 1, "Кнопка отсутствует на странице"
    time.sleep(3)
