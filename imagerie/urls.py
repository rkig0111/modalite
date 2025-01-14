from django.contrib import admin
from django.urls import path
from . import views 
# from .views import PingView

app_name = 'imagerie'

urlpatterns = [
    path("", views.show_all_modalite , name='show_all_modalite' ),
    path("show/<int:id>/", views.show_modalite , name='show_modalite' ),
    # path("edit/<int:id>/", views.edit_modalite , name='edit_modalite' ),
    # path("delete/<int:id>/", views.delete_modalite , name='delete_modalite' ), 
    # ath("ping/", views.Ping , name='ping' ), 
    # ath("ping2/", views.Ping2 , name='ping2' ),
    # ath("ping3/", views.Ping3 , name='ping3' ),
    path("ajax/", views.Ajax , name='ajax' ),
    path("test/", views.test , name='test' ), 
    path("inc/", views.Inc , name='inc' ), 
]