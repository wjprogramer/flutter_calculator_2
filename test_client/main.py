import pytest
import os

if __name__ == '__main__':
    print("Run pytest")
    pytest.main(args=[
        '-s',
        '-v',  # verbose: 顯示更多資訊
        '-rA',  # 同時顯示測試結果為錯誤和正確的資訊
        '--clean-alluredir',  # [allure] 清除之前的 json 報告
        r'--alluredir=report/json',  # [allure] 產生 json 報告
    ])

    # [allure] 將 json 轉成 html
    os.system('allure generate ./report/json -o ./report/html -c')
