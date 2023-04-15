# from django.urls import path, include

from currency.api.views import ContactUsViewSet  # ContactUsCreateApiView, ContactUsApiView
from rest_framework.routers import DefaultRouter

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'contactus', ContactUsViewSet, basename='contactus')

urlpatterns = [
    # path('sources/', SourceApiView.as_view(), name='sources'),
    # path('contact-us/create/', ContactUsViewSet.as_view({'post': 'create'}), name='contact-us-create'),
    # path('contact-us/', ContactUsViewSet.as_view({'get': 'list'}), name='contact-us'),
    # path('contact-us/<int:pk>/', ContactUsViewSet.as_view({'put': 'update'}), name='contact-us-update'),
    # path('contact-us/delete/<int:pk>/', ContactUsViewSet.as_view({'delete': 'destroy'}), name='contact-us-delete')

]
urlpatterns += router.urls
