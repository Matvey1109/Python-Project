from django.urls import path
from . import views
from .views import Sign_Up
from .views import Registration
from .views import Logout

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('registration/', Registration.as_view(), name="registration"),
    path('sign_up/', Sign_Up.as_view(), name="sign_up"),
    path('logout/', Logout.as_view(), name='logout'),
]