from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add_player/', views.add_player, name='add_player'),
    path('game/', views.play_game, name="game"),
    path('admin/', views.admin, name="admin"),
    path('play_game/', views.play_game, name="play_game"),
    path('random_word/', views.random_word, name="random_word")
]