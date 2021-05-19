from django.urls import path
from django.views.generic import RedirectView
from . import views


app_name = 'data_manage'

urlpatterns = [
    path('data_manage/', views.data_manage_index, name='data_manage_index'),
    path('data_manage_show/', views.data_manage_show, name='data_manage_show'),
    path('', RedirectView.as_view(url='data_manage/')),
]