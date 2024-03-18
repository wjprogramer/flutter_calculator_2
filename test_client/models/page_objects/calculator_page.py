from appium import webdriver
from appium.webdriver.webdriver import By


# Page Object
class CalculatorPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def click_number(self, number: int):
        self.driver.find_element(By.ID, f'qa_{number}_btn').click()

    def click_plus(self):
        self.driver.find_element(By.ID, 'qa_plus_btn').click()

    def click_minus(self):
        self.driver.find_element(By.ID, 'qa_minus_btn').click()

    def click_equal(self):
        self.driver.find_element(By.ID, 'qa_equal_btn').click()

    def get_result(self):
        return self.driver.find_element(By.ID, 'qa_answer').text
