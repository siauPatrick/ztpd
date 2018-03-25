from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView, TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('favicon.ico', RedirectView.as_view(url=f'{settings.STATIC_URL}favicon.ico', permanent=True)),
    path('admin/', admin.site.urls),
]
