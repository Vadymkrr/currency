from django.http import HttpResponse
from currency.models import Rate, ContactUs
from django.shortcuts import render


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }
    return render(request, 'rates_list.html', context)


def query_list(request):

    contacts = ContactUs.objects.all()

    context = {
        'contacts': contacts
    }
    return render(request, 'contact_us.html', context)


def status_code(request):

    response = HttpResponse(
        'Not found',
        status=404,
    )
    return response
