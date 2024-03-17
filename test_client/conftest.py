import time
from typing import Optional

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

driver: Optional[webdriver.Remote] = None
appium_server_url = 'http://localhost:4723'

deviceCapabilities = {
    # -- Device 設定 ------------------------------------------------
    'deviceName': 'R5CT20DXADK',  # 透過指令 adb devices 取得
    'platformVersion': '14',  # 需要看對應的裝置手機版本
    # ---------------------------------------------------------------
    'appPackage': 'com.example.flutter_calculator_2',
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'appActivity': '.MainActivity',
    'autoGrantPermissions': True,
    'appium:disableIdLocatorAutocompletion': True,
}


# 啟動 App
@pytest.fixture()
def start_app():
    global driver
    driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(deviceCapabilities)
    )
    return driver


# 關閉 App
@pytest.fixture()
def close_app():
    yield driver
    time.sleep(1)
    driver.quit()
