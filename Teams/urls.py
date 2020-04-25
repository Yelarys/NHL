from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   # path('', views.TeamsView.as_view()),

    path('Teams/', views.team_list),
    path('Teams/list/', views.TeamList.as_view()),
    path('Teams/detail/<int:pk>/', views.TeamDetailView.as_view()),

    path('players/', views.player_list),
    path('players/list/', views.PlayerList.as_view()),
    path('players/detail/<int:pk>/', views.PlayerDetailView.as_view()),

    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
