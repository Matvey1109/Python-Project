from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    full_name = models.CharField(max_length=60)
    relationship = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class ContactPermissions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whom')