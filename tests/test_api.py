def test_get_currency_rate(test_currency):
    assert test_currency.get_rate('byn') == 0.02
    assert test_currency.get_rate('byr') == 0.02
    assert test_currency.get_rate('usd') == 0.01
