from django.http import HttpResponse

from currency.models import Rate, ContactUs


def list_rates(request):
    qs = Rate.objects.all()
    result = []

    for rate in qs:
        result.append(
            f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency},'
            f' source: {rate.source}, created: {rate.created} <br>')

    return HttpResponse(str(result))


def query_list(request):
    qs = ContactUs.objects.all()
    result = []

    for contact in qs:
        result.append(
            f'id: {contact.id}, email: {contact.email_from}, subject: {contact.subject}, '
            f'message: {contact.message} <br>')

    return HttpResponse(str(result))


def status_code(request):

    response = HttpResponse(
        'Not found',
        status=404,
    )
    return response
