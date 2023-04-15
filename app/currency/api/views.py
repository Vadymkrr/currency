from rest_framework import generics, viewsets

from currency.models import Source, ContactUs

from currency.api.serializers import SourceSerializer, ContactUsSerializer

from currency.paginators import SourcesPagination, ContactUsPagination
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.filters import SourceFilter, ContactUsFilter


class SourceApiView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    pagination_class = SourcesPagination
    # permission_classes = (AllowAny)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = SourceFilter
    ordering_fields = ('id', 'name')


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = ContactUsPagination

    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )

    filterset_class = ContactUsFilter
    ordering_fields = ('id', 'email_from', 'message')

# class ContactUsApiView(generics.ListAPIView):
#     queryset = ContactUs.objects.all()
#     serializer_class = ContactUsSerializer
#
#
# class ContactUsCreateApiView(generics.CreateAPIView):
#     queryset = ContactUs.objects.all()
#     serializer_class = ContactUsSerializer
#
#
# class ContactUsAPIRUDView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ContactUs.objects.all()
#     serializer_class = ContactUsSerializer
