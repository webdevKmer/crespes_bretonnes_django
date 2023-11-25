from django.urls import path
from . import views
from datetime import datetime


urlpatterns = [
    path('', views.home, name='home'),
    # path('<article_id>/', views.detail, name='detail'),
    path('date/', views.heure_actuelle, name='heure'),
    path('add/<num1>/<num2>/', views.addition, name='addition'),
]