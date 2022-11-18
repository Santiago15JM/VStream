from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='Home'),
               path('player/<int:vid>', views.player, name='Player'),
               path('addcomment/<int:vid>', views.addComment, name='Add comment'),
               path('savecomment/<int:vid>', views.saveComment, name='Save comment'),
               path('search/', views.search, name='Search'),
               ]
