def test_sample_1():
    a = 5
    b = 10
    # assert: 驗證程式是否符合預期的結果
    # 可加上錯誤時的提示訊息，方便閱讀測試報告
    assert a == b, 'a is not equal to b'


def test_sample_2():
    a = 3
    b = 7
    assert a < b


def test_sample_3():
    a = 'Hello'
    b = 'World'
    assert a != b
