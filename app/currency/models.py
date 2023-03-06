from django.db import models

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}, Sell: {self.sell},Source: {self.source}'


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=255)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'ID: {self.id}, Email: {self.email_from}, Subject: {self.subject}, Message: {self.message}'


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'ID: {self.id}, URL: {self.source_url}, Name: {self.name}, Country: {self.country}'
