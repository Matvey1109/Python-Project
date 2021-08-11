from django.urls import path
from . import views

urlpatterns = [
    path('', views.translate, name='translate'),
    path('translated/', views.translated, name='translated'),
]