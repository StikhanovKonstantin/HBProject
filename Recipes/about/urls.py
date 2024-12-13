from django.urls import path

from . import views


# Пространство имён.
app_name = 'about'

urlpatterns: list = [
    path('', views.get_about, name='get_about'),
]