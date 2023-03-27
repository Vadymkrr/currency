from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from currency.models import (
    Source,
    Rate,
    ContactUs,
    RequestResponseLog,
)


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'country',
            'avatar',
        )


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency',
            'buy',
            'sell',
            'source',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )


class RequestResponseLogForm(forms.ModelForm):
    class Meta:
        model = RequestResponseLog
        fields = (
            'path',
            'request_method',
            'time',
        )
