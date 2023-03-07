from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter
from currency.models import Rate, Source, ContactUs


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'currency',
        'buy',
        'sell',
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
    list_filter = (
        'name',
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
    list_filter = (
        'subject',
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
