import allure
import pytest

from models.page_objects.calculator_page import CalculatorPage
from appium import webdriver


# 記得 class 要以 Test 開頭
@pytest.mark.usefixtures('setup_and_teardown')
@allure.epic('計算機')
@allure.feature('v1.0')
class TestSubAdd:
    driver: webdriver.Remote

    @allure.story('加法運算')
    @allure.title('驗證計算機能否正常完成加法功能')
    def test_add(self):
        calc_page = CalculatorPage(self.driver)

        with allure.step('依序按下1、+、2、='):
            calc_page.click_number(1)
            calc_page.click_plus()
            calc_page.click_number(2)
            calc_page.click_equal()
            actual_result = calc_page.get_result()
        with allure.step('驗證實際結果是否正確'):
            assert actual_result == '=3'
        calc_page.add_screenshot_attach('加法運算結果')

    @allure.story('減法運算')
    @allure.title('驗證計算機能否正常完成減法功能')
    def test_sub(self):
        calc_page = CalculatorPage(self.driver)

        with allure.step('依序按下5、-、3、='):
            calc_page.click_number(5)
            calc_page.click_minus()
            calc_page.click_number(3)
            calc_page.click_equal()
            actual_result = calc_page.get_result()
        with allure.step('驗證實際結果是否正確'):
            assert actual_result == '=1', '結果不為1'
