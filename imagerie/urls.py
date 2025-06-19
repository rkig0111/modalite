from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from django.urls import re_path
from . import views 
# from .views import PingView

app_name = 'imagerie'

urlpatterns = [ 
    # path("", RedirectView.as_view(url='admin/imagerie/modalite/') ),
    path("", RedirectView.as_view(url='biomed_modalite/imagerie/modalite/') ), 
    # path("", RedirectView.as_view(url='admin/imagerie/modalite/?q=&reforme__exact=0') ),
    #path("", RedirectView.as_view(url='biomed_modalite/imagerie/modalite/?_facets=True&reforme=0') ),
    # path("", RedirectView.as_view(url='admin/') ),
    path("index", views.index, name='index' ),
    path("all", views.show_all_modalite , name='show_all_modalite' ),
    path("show/<int:id>/", views.show_modalite , name='show_modalite' ),
    path("detail_modalite/<int:id>/", views.detail_modalite , name='detail_modalite' ),
    path("show_appareiltype/<int:id>/", views.show_appareiltype , name='show_appareiltype' ),
    # path("edit/<int:id>/", views.edit_modalite , name='edit_modalite' ),
    # path("delete/<int:id>/", views.delete_modalite , name='delete_modalite' ), 
    # path("ping3/", views.Ping3 , name='ping3' ),
    path("test/", views.test , name='test' ),     
    re_path(r'^(?P<ip>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', views.pingip, name='pingip' ),
    # path(r'^(?P<post_id>[0-9]+)', views.pingip, name='pingip' ),
    # path(r'^(?P<ip>(?:(?:0|1[\d]{0,2}|2(?:[0-4]\d?|5[0-5]?|[6-9])?|[3-9]\d?)\.){3}(?:0|1[\d]{0,2}|2(?:[0-4]\d?|5[0-5]?|[6-9])?|[3-9]\d?))/(?P<pseudo>\w+)/$',  views.pingip, name='pingip' ),
]