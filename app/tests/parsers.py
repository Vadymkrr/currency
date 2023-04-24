from unittest.mock import MagicMock

from currency.tasks import parse_monobank

from currency.models import Rate


def test_monobank_parser(mocker):
    initial_count = Rate.objects.count()
    monobank_data = [{
        "currencyCodeA": 840,
        "currencyCodeB": 980,
        "date": 1682287274,
        "rateBuy": 36.65,
        "rateCross": 0,
        "rateSell": 37.4406},
        {"currencyCodeA": 978,
         "currencyCodeB": 980,
         "date": 1682341274,
         "rateBuy": 40.35,
         "rateCross": 0,
         "rateSell": 41.5007}
    ]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: monobank_data
        )
    )
    parse_monobank()

    assert Rate.objects.count() == initial_count + 2
