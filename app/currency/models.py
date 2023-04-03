from django.db import models
from django.templatetags.static import static

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}, Sale: {self.sale},Source: {self.source}'


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=255)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f'ID: {self.id}, Email: {self.email_from}, Subject: {self.subject}, Message: {self.message}'


def avatar_path(instance, filename):
    return f'avatars/{instance.id}/{filename}'


class Source(models.Model):
    source_url = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    avatar = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=avatar_path
    )
    code_name = models.CharField(max_length=64, unique=True)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('privat.jpg')

    def __str__(self):
        return f'{self.name}'


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(
        max_length=255,
    )
    time = models.FloatField()

    class Meta:
        verbose_name = 'Request, Response, Log'
        verbose_name_plural = 'Request, Response, Log'

    def __str__(self):
        return f'ID: {self.id}, Path: {self.path}, Request method: {self.request_method}'
