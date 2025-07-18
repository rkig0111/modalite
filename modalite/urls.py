from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import RedirectView
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings
from imagerie import views

app_name = 'modalite'

urlpatterns = [
    path("", include('imagerie.urls') ),
    path("api-auth/", include('rest_framework.urls') ),
    # path("admin/", admin.site.urls),
    path("biomed_modalite/", admin.site.urls),
    path('signup', views.signup, name="signup"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    # path("imagerie/", include('imagerie.urls') ),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
