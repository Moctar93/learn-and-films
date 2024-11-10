# films/urls.py
from django.urls import path
from . import views
from .views import film_list

urlpatterns = [
        path('add-film-api/', views.add_film_api, name='add-film-api'),
        path('add-film/', views.add_film, name='add-film'),
        path('list/', film_list, name='film_list'),
        path('<int:film_id>/play/', views.play_film, name='play_film'),
]

