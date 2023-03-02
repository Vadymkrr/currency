from django.http import HttpResponse
from currency.models import Rate, ContactUs, Source
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from currency.forms import SourceForm, RateForm, ContactUsForm
from django.shortcuts import render


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all()


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('rate-list')


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('rate-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('rate-list')
    queryset = Rate.objects.all()


class ContactUsListView(ListView):
    template_name = 'contact_us_list.html'
    queryset = ContactUs.objects.all()


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contact_us_create.html'
    success_url = reverse_lazy('contact-list')


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contact_us_update.html'
    success_url = reverse_lazy('contact-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us_delete.html'
    success_url = reverse_lazy('contact-list')


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us_details.html'


class SourceListView(ListView):
    template_name = 'source_list.html'
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('source-list')
    queryset = Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('source-list')


def status_code(request):
    response = HttpResponse(
        'Not found',
        status=404,
    )
    return response
