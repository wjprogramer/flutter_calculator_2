from appium import webdriver
from appium.webdriver.webdriver import By


class BasePage:
    """
    基礎的 Page Object 模型
    封裝一些常用方法
    """

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def by_id(self, id_):
        return self.driver.find_element(By.ID, id_)

