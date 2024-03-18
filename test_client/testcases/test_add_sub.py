import allure
from appium.webdriver.webdriver import By


# 記得 class 要以 Test 開頭
@allure.epic('計算機')
@allure.feature('v1.0')
class TestSubAdd:

    @allure.story('加法運算')
    @allure.title('驗證計算機能否正常完成加法功能')
    def test_add(self, start_app, close_app):
        with allure.step('啟動 App'):
            driver = start_app
        with allure.step('依序按下1、+、2、='):
            driver.find_element(By.ID, 'qa_1_btn').click()
            driver.find_element(By.ID, 'qa_plus_btn').click()
            driver.find_element(By.ID, 'qa_2_btn').click()
            driver.find_element(By.ID, 'qa_equal_btn').click()
            actual_result = driver.find_element(By.ID, 'qa_answer').text
        with allure.step('驗證實際結果是否正確'):
            assert actual_result == '=3'

        # 附上截圖
        # （可以將 attach 縮排，會將結果附於 step 裡）
        allure.attach(
            driver.get_screenshot_as_png(),
            name='加法運算結果',
            attachment_type=allure.attachment_type.PNG
        )

    @allure.story('減法運算')
    @allure.title('驗證計算機能否正常完成減法功能')
    def test_sub(self, start_app, close_app):
        with allure.step('啟動 App'):
            driver = start_app
        with allure.step('依序按下5、-、3、='):
            driver.find_element(By.ID, 'qa_5_btn').click()
            driver.find_element(By.ID, 'qa_minus_btn').click()
            driver.find_element(By.ID, 'qa_3_btn').click()
            driver.find_element(By.ID, 'qa_equal_btn').click()
            actual_result = driver.find_element(By.ID, 'qa_answer').text
        with allure.step('驗證實際結果是否正確'):
            assert actual_result == '=1', '結果不為1'
