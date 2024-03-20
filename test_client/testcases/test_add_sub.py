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

    @allure.story('加法運算')
    @allure.title('相同數字進行加法運算')
    @pytest.mark.parametrize("n,expected", [(1, 2), (2, 4), (3, 6)])
    def test_add_same_number(self, n, expected):
        calc_page = CalculatorPage(self.driver)

        with allure.step(f'依序按下{n}、+、{n}、='):
            calc_page.click_number(n)
            calc_page.click_plus()
            calc_page.click_number(n)
            calc_page.click_equal()
            actual_result = calc_page.get_result()
        with allure.step('驗證實際結果是否正確'):
            assert actual_result == f'={expected}', f'結果不為{expected}'

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

    @pytest.mark.parametrize("x", [5,  2])
    @pytest.mark.parametrize("y", [2,  3])
    def test_sub_others(self, x, y):
        calc_page = CalculatorPage(self.driver)
        expected = x - y

        with allure.step(f'依序按下{x}、-、{y}、='):
            calc_page.click_number(x)
            calc_page.click_minus()
            calc_page.click_number(y)
            calc_page.click_equal()
            actual_result = calc_page.get_result()
        with allure.step('驗證實際結果是否正確'):
            assert actual_result == f'={expected}', f'結果不為{expected}'
        calc_page.add_screenshot_attach(f'減法運算結果{x}-{y}={expected}')
