import pytest

if __name__ == '__main__':
    print("Run pytest")
    pytest.main(args=[
        '-v',  # verbose: 顯示更多資訊
        '-rA',  # 同時顯示測試結果為錯誤和正確的資訊
    ])
