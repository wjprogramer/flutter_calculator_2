import time
from typing import Optional

import allure
import pytest
from pytest import FixtureRequest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from src.utils import load_capabilities

driver: Optional[webdriver.Remote] = None
appium_server_url = 'http://localhost:4723'

deviceCapabilities = {
    # -- Device 設定 ------------------------------------------------
    'deviceName': '',  # 透過指令 adb devices 取得
    'platformVersion': '',  # 需要看對應的裝置手機版本
    'platformName': '',
    # ---------------------------------------------------------------
    'appPackage': 'com.example.flutter_calculator_2',
    'automationName': 'uiautomator2',
    'appActivity': '.MainActivity',
    'autoGrantPermissions': True,
    'appium:disableIdLocatorAutocompletion': True,
}

deviceCapabilities.update(load_capabilities()[0])


# 啟動 App -> 執行 -> 關閉 App
@pytest.fixture(scope='function')
def setup_and_teardown(request: FixtureRequest):
    global driver
    driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(deviceCapabilities)
    )
    # 設定 class 的 property
    request.cls.driver = driver
    yield
    time.sleep(1)
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        # 將錯誤截圖附於測試報告
        driver.save_screenshot('report/' + item.name + '.png')
        allure.attach.file('report/' + item.name + '.png', attachment_type=allure.attachment_type.PNG)
        # 將錯誤訊息附於測試報告
        allure.attach(report.longreprtext, attachment_type=allure.attachment_type.TEXT)
