from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter
from currency.models import Rate, Source, ContactUs, RequestResponseLog


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'currency',
        'buy',
        'sale',
        'source',
        'created',
    )
    list_filter = (
        'currency',
        'source',
        ('created', DateRangeFilter),
    )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
        'country',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'country',
    )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
    )
    search_fields = (
        'subject',
    )
    list_filter = (
        'email_from',
    )
    readonly_fields = (
        'id',
        'email_from',
        'subject',
        'message',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'request_method',
        'time',
    )
    search_fields = (
        'request_method',
    )

    def has_add_permission(self, request):
        return False
