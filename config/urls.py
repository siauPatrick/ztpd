from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView, TemplateView

from citizens.views import CitizenListAPIView

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('api/citizens/', CitizenListAPIView.as_view(), name='citizens'),
    path('favicon.ico', RedirectView.as_view(url=f'{settings.STATIC_URL}favicon.ico', permanent=True)),
    path('admin/', admin.site.urls),
]
