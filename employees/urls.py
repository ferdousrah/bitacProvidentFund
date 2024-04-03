from django.urls import path
from employees import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Index
    #path('', views.index, name="index"),

    # Pages
    path('dashboard/', views.dashboard, name="dashboard"),
    
]
