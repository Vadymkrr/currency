from django.urls import path

from currency.views import (
    status_code,

    RateListView,
    RateCreateView,
    RateDetailView,
    RateDeleteView,
    RateUpdateView,

    ContactUsListView,
    ContactUsCreateView,
    ContactUsUpdateView,
    ContactUsDeleteView,
    ContactUsDetailView,

    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailView,

    RequestResponseLogListView,
    RequestResponseLogDeleteView,
)


urlpatterns = [
    path('status1/', status_code),

    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),

    path('contact/list/', ContactUsListView.as_view(), name='contact-list'),
    path('contact/create/', ContactUsCreateView.as_view(), name='contact-create'),
    path('contact/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contact-update'),
    path('contact/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contact-delete'),
    path('contact/details/<int:pk>/', ContactUsDetailView.as_view(), name='contact-details'),

    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

    path('req-res/list/', RequestResponseLogListView.as_view(), name='req-res-list'),
    path('req-res/delete/<int:pk>/', RequestResponseLogDeleteView.as_view(), name='req-res-delete')
]
