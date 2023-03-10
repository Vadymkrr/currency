from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'
    UAH = 3, 'Hryvnia'


class RequestResponseLogChoices(models.TextChoices):
    GET = 'GET',
    POST = 'POST'
