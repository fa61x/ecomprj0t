from django.urls import path
from . import views

app_name = 'kkart'

urlpatterns = [
    path('', views.fun, name='fun')

]
