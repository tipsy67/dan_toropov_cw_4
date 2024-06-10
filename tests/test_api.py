def test_get_currency_rate(currency):
    """

    :param currency:
    :return:
    """
    assert currency.get_rate('byn') == 0.02
    assert currency.get_rate('byr') == 0.02
    assert currency.get_rate('usd') == 0.01

