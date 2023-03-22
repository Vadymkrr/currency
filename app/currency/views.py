from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from currency.models import Rate, ContactUs, Source, RequestResponseLog
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from currency.forms import SourceForm, RateForm, ContactUsForm, RequestResponseLogForm


class IndexView(TemplateView):
    template_name = 'currency:index.html'


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all().select_related('')


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(ListView):
    template_name = 'contact_us_list.html'
    queryset = ContactUs.objects.all()


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contact_us_create.html'
    success_url = reverse_lazy('currency:contact-list')

    def _send_email(self):
        subject = 'User ContactUs'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
            Request from: {self.object.email_from}.
            Reply too email: {self.object.email_from}.
            Subject: {self.object.subject}.
            Body: {self.object.message}
        '''

        from django.core.mail import send_mail
        send_mail(
            subject,
            message,
            recipient,
            [recipient],
            fail_silently=False
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'contact_us_update.html'
    success_url = reverse_lazy('currency:contact-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us_delete.html'
    success_url = reverse_lazy('currency:contact-list')


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us_details.html'


class SourceListView(ListView):
    template_name = 'source_list.html'
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')


class RequestResponseLogListView(ListView):
    template_name = 'req-res-log_list.html'
    queryset = RequestResponseLog.objects.all()


class RequestResponseLogCreateView(CreateView):
    form_class = RequestResponseLogForm
    template_name = 'req-res-log_create.html'
    success_url = reverse_lazy('currency:req-res-list')


class RequestResponseLogDeleteView(DeleteView):
    queryset = RequestResponseLog.objects.all()
    template_name = 'req-res-log_delete.html'
    success_url = reverse_lazy('currency:req-res-list')


def status_code(request):
    response = HttpResponse(
        'Not found',
        status=404,
    )
    return response


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')
    queryset = get_user_model().objects.all()
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset
