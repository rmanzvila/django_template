# -*- encoding:utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

admin.site.site_header = 'Ricardo Manzanares Avila'
admin.site.site_title = 'Ricardo Manzanares Avila'
admin.site.index_title = 'Ricardo Manzanares Avila'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
