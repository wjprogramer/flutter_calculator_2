from appium.webdriver.webdriver import By


# 記得 class 要以 Test 開頭
class TestSubAdd:
    def test_add(self, start_app, close_app):
        driver = start_app
        driver.find_element(By.ID, 'qa_1_btn').click()
        driver.find_element(By.ID, 'qa_plus_btn').click()
        driver.find_element(By.ID, 'qa_2_btn').click()
        driver.find_element(By.ID, 'qa_equal_btn').click()
        actual_result = driver.find_element(By.ID, 'qa_answer').text
        assert actual_result == '=3'
