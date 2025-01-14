from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings

app_name = 'modalite'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("imagerie/", include('imagerie.urls') ),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
