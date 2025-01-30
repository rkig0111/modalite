from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from . import views 
# from .views import PingView

app_name = 'imagerie'

urlpatterns = [    
    path("", RedirectView.as_view(url='admin/') ),
    path("index", views.index, name='index' ),
    path("all", views.show_all_modalite , name='show_all_modalite' ),
    path("show/<int:id>/", views.show_modalite , name='show_modalite' ),
    path("detail_modalite/<int:id>/", views.detail_modalite , name='detail_modalite' ),
    path("show_appareiltype/<int:id>/", views.show_appareiltype , name='show_appareiltype' ),
    # path("edit/<int:id>/", views.edit_modalite , name='edit_modalite' ),
    # path("delete/<int:id>/", views.delete_modalite , name='delete_modalite' ), 
    # path("ping3/", views.Ping3 , name='ping3' ),
    path("test/", views.test , name='test' ), 
]