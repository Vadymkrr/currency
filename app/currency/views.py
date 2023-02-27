from django.http import HttpResponse, HttpResponseRedirect
from currency.models import Rate, ContactUs, Source
from currency.forms import SourceForm
from django.shortcuts import render, get_object_or_404


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


def list_source(request):
    sources = Source.objects.all()

    context = {
        'sources': sources
    }
    return render(request, 'source_list.html', context)


def details_source(request, pk):
    source = get_object_or_404(Source, pk=pk)
    context = {
        'source': source
    }
    return render(request, 'details_source.html', context)


def create_source(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form
    }
    return render(request, 'create_source.html', context)


def update_source(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form
    }
    return render(request, 'update_source.html', context)


def delete_source(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        context = {
            'source': source
        }
        return render(request, 'delete_source.html', context)


def status_code(request):
    response = HttpResponse(
        'Not found',
        status=404,
    )
    return response
