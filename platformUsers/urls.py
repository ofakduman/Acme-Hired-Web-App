from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('search/', views.search, name= "search"),
    path('results/', views.results, name= "results"),
    path('results2/', views.results2, name= "results2"),
    path('profile_card/<username>/', views.profile_card, name= "profile_card"),
    path('profile_card/', views.profile_card, name= "profile_card"),
    path('fav_history/', views.fav_history, name= "fav_history"),

]