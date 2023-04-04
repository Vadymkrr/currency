from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django import forms

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
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        'currency',
        'buy',
        'sale',
        'source',
        Submit('submit', 'Save changes'),
        HTML('<a class="btn btn-default" href="{% url "currency:rate-list" %}">Cancel</a>')
    )

    class Meta:
        model = Rate
        fields = (
            'currency',
            'buy',
            'sale',
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
