"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from currency.views import (
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

    #query_list,
    status_code,

    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include('debug_toolbar.urls')),

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

    path('status1/', status_code),

    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete')
]
