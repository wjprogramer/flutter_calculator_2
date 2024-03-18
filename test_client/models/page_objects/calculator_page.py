from models.page_objects.base.base_page import BasePage


# Page Object
class CalculatorPage(BasePage):

    def click_number(self, number: int):
        self.by_id(f'qa_{number}_btn').click()

    def click_plus(self):
        self.by_id('qa_plus_btn').click()

    def click_minus(self):
        self.by_id('qa_minus_btn').click()

    def click_equal(self):
        self.by_id('qa_equal_btn').click()

    def get_result(self):
        return self.by_id('qa_answer').text
