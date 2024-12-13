from django.urls import path

from . import views


# Пространство имён.
app_name = 'homepage'

urlpatterns = [
    path('', views.get_homepage, name='get_homepage'),
]