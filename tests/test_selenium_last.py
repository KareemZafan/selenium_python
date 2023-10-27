# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest

# driver = webdriver.Chrome()
# driver.maximize_window()


# def test_drag_and_drop():
#     driver.get("https://demo.guru99.com/test/drag_drop.html")
#     amount = driver.find_element(By.CSS_SELECTOR, "#products ul li:nth-child(2)")
#     bank = driver.find_element(By.CSS_SELECTOR, "#products ul li:nth-child(5)")
#     bank_place = driver.find_element(By.ID, "bank")
#     amount_place = driver.find_element(By.ID, "amt7")
#     actions = ActionChains(driver)
#     actions.drag_and_drop(amount, amount_place).perform()
#     actions.drag_and_drop(bank, bank_place).perform()

#     assert driver.find_element(By.ID, "t7").text == "5000"


# def test_hovers():
#     driver.get("https://the-internet.herokuapp.com/hovers")
#     action = ActionChains(driver)
#     action.move_to_element(driver.find_element(By.XPATH, "(//img[@alt='User Avatar'])[1]")).perform()
#     user_name = driver.find_element(By.XPATH, "//h5[text()='name: user1']")
#     assert user_name.is_displayed()


def test_workflow():
    assert 1 == 1 
    assert 2 - 2 == 0 
    
def test_failure():
    assert len("Kareem") == 6
