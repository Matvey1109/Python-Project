from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('contact_profile/<str:pk>', views.contact_profile, name='contact_profile'),
    path('edit_contact/<str:pk>', views.edit_contact, name='edit_contact'),
    path('delete_contact/<str:pk>', views.delete_contact, name='delete_contact')
]
