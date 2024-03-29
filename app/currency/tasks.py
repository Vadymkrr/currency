from celery import shared_task
from django.conf import settings
from currency.choices import RateCurrencyChoices
import requests

from currency.constants import (
    PRIVATBANK_CODE_NAME,
    MONOBANK_CODE_NAME,
)
from currency.utils import to_2_places_decimal


@shared_task()
def parse_monobank():
    from currency.models import Rate, Source

    source, _ = Source.objects.get_or_create(
        code_name=MONOBANK_CODE_NAME,
        defaults={
            'name': 'mono',
            'source_url': 'https://www.monobank.ua'
        }
    )

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        840: RateCurrencyChoices.USD,
        978: RateCurrencyChoices.EUR,
        980: RateCurrencyChoices.UAH,
    }

    for rate in rates:
        if rate['currencyCodeA'] not in available_currency:
            continue
        if rate['currencyCodeA'] != 980 and rate['currencyCodeB'] != 980:
            continue

        buy = to_2_places_decimal(rate['rateBuy'])
        sale = to_2_places_decimal(rate['rateSell'])

        last_rate = Rate.objects.filter(
            currency=available_currency[rate['currencyCodeA']],
            source=source
        ) \
            .order_by('-created') \
            .last()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[rate['currencyCodeA']],
                source=source
            )


@shared_task()
def parse_privatbank():
    from currency.models import Rate, Source

    # source = Source.objects.filter(code_name=PRIVATBANK_CODE_NAME).first()
    #
    # if source is None:
    #     source = Source.objects.create(code_name=PRIVATBANK_CODE_NAME, name='PB')

    source, _ = Source.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PB',
            'source_url': 'https://privatbank.ua'
        }
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        buy = to_2_places_decimal(rate['buy'])
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ) \
            .order_by('-created') \
            .last()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task()
def send_mail(subject, message):
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False
    )
