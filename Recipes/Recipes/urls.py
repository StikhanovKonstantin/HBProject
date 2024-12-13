from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('recipes/', include('recipesapp.urls', namespace='recipesapp')),
    path('about/', include('about.urls', namespace='about'))
]
