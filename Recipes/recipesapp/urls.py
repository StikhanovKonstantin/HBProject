from django.urls import path

from . import views


# Пространство имён.
app_name = 'recipesapp'

urlpatterns = [
    path('', views.get_recipes, name="get_recipes"),
    path('recipe/<int:recipe_id>/', views.current_recipe, name='current_recipe'),
]